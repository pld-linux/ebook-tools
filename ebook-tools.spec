Summary:	Tools for accessing and converting ebook file formats
Summary(pl.UTF-8):	Narzędzia do odczytu i konwersji formatów plików ebooków
Name:		ebook-tools
Version:	0.2.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/ebook-tools/%{name}-%{version}.tar.gz
# Source0-md5:	67bce67ceb72dcc3578d6a81ef92b29b
URL:		http://ebook-tools.sourceforge.net/
BuildRequires:	cmake >= 2.4.0
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
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files for ebook-tools libepub library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe biblioteki libepub z pakietu
ebook-tools.

%prep
%setup -q

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
%doc LICENSE README TODO
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
