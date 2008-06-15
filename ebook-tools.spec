Summary:	ebook tools
Summary(pl.UTF-8):	ebook tools
Name:		ebook-tools
Version:	0.1.0
Release:	1
License:	GPL v3
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/ebook-tools/%{name}-%{version}.tar.gz
# Source0-md5:	020d8bc5b718a9e09242900a496cda8a
URL:		http://www.
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ebook-tools.

%description -l pl.UTF-8
ebook-tools.

%prep
%setup -q

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	.
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/plasma_applet_wifi_signal.so
%attr(755,root,root) %{_bindir}/einfo
%attr(755,root,root) %{_bindir}/lit2epub
%{_includedir}/epub.h
%{_includedir}/epub_shared.h
%attr(755,root,root) %{_libdir}/libepub.so
%attr(755,root,root) %{_libdir}/libepub.so.0
%attr(755,root,root) %{_libdir}/libepub.so.0.1.0
