Summary:	tools for accessing and converting ebook file formats
Summary(pl.UTF-8):	tools for accessing and converting ebook file formats
Name:		ebook-tools
Version:	0.1.1
Release:	1
License:	GPL v3
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/ebook-tools/%{name}-%{version}.tar.gz
# Source0-md5:	15946af6f946eabe8247cdef9ada2b88
URL:		http://sourceforge.net/projects/ebook-tools
BuildRequires:	cmake
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ebook-tools provides tools for accessing and converting various ebook
file formats.

%description -l pl.UTF-8
ebook-tools provides tools for accessing and converting various ebook
file formats.

%package devel
Summary:	ebook-tools - header files
Summary(pl.UTF-8):	ebook-tools - pliki nagłówkowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files for ebook-tools.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe do ebook-tools.

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
%attr(755,root,root) %{_bindir}/einfo
%attr(755,root,root) %{_bindir}/lit2epub
%attr(755,root,root) %ghost %{_libdir}/libepub.so.?
%attr(755,root,root) %{_libdir}/libepub.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepub.so
%{_includedir}/epub.h
%{_includedir}/epub_shared.h
