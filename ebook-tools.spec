Summary:	Tools for accessing and converting ebook file formats
Summary(pl.UTF-8):	Narzędzia do odczytu i konwersji formatów plików ebooków
Name:		ebook-tools
Version:	0.2.1
Release:	2
License:	GPL v3
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/ebook-tools/%{name}-%{version}.tar.gz
# Source0-md5:	cabbd2ef9148a61ca5f6e60ca63e6045
Patch0:		%{name}-lib64.patch
URL:		http://ebook-tools.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	libxml2-devel
BuildRequires:	libzip-devel
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ebook-tools provides tools for accessing and converting various ebook
file formats.

%description -l pl.UTF-8
Pakiet ebook-tools dostarcza narzędzia do odczytu i konwersji różnych
formatów plików ebooków.

%package devel
Summary:	ebook-tools - header files for libepub library
Summary(pl.UTF-8):	ebook-tools - pliki nagłówkowe biblioteki libepub
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files for ebook-tools libepub library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe biblioteki libepub z pakietu
ebook-tools.

%prep
%setup -q
%patch0 -p0

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_CXX_COMPILER_WORKS=1 \
	-DCMAKE_CXX_COMPILER="%{__cc}" \
	-DCMAKE_VERBOSE_MAKEFILE=1 \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/einfo
%attr(755,root,root) %{_bindir}/lit2epub
%attr(755,root,root) %{_libdir}/libepub.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libepub.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepub.so
%{_includedir}/epub.h
%{_includedir}/epub_shared.h
%{_includedir}/epub_version.h
