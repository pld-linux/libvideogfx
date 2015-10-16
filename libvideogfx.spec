#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	LibVideoGfx - video processing library
Summary(pl.UTF-8):	LibVideoGfx - biblioteka do przetwarzania obrazu
Name:		libvideogfx
Version:	1.0.9
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/farindk/libvideogfx/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e60c78bce880264572203fcdb208da79
Patch0:		%{name}-sh.patch
Patch1:		%{name}-gcc.patch
Patch2:		%{name}-ffmpeg.patch
Patch3:		%{name}-link.patch
Patch4:		%{name}-m4.patch
URL:		http://dirk-farin.net/software/libvideogfx/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ffmpeg-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 6:4.5
BuildRequires:	libtool >= 2:1.5
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibVideoGfx is a C++ library for low-level video processing. It aims
at speeding up the development process for image and video processing
applications by providing high-level classes for commonly required
tasks. The library comprises support for:
 - basic image data classes
 - color-space convertion for RGB, YUV, HSV
 - drawing primitives (lines, circles, ...)
 - image manipulation (scaling, pixel-ops, convolution)
 - file-IO (ppm, yuv, jpeg, png, mpeg, V4L-grabbing)
 - X11 image display (including Xv-extension support)

%description -l pl.UTF-8
LibVideoGfx to biblioteka C++ do niskopoziomowego przetwarzania
obrazu. Celem jest przyspieszenie procesu tworzenia aplikacji do
przetwarzania obrazu statycznego i ruchomego poprzez dostarczenie
wysokopoziomowych klas do często wymaganych zadań. Biblioteka pokrywa:
 - podstawowe klasy danych obrazu
 - konwersję przestrzeni kolorów RGB, YUV, HSV
 - prymitywy rysunkowe (linie, okręgi...)
 - obróbkę obrazu (skalowanie, operacje na pikselach, sploty)
 - operacje na plikach (ppm, yuv, jpeg, png, mpeg, przechwytywanie
   V4L)
 - wyświetlanie obrazu X11 (wraz z obsługą rozszerzenia Xv)

%package devel
Summary:	Header files for LibVideoGfx library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LibVideoGfx
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.5
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXv-devel

%description devel
Header files for LibVideoGfx library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LibVideoGfx.

%package static
Summary:	Static LibVideoGfx library
Summary(pl.UTF-8):	Statyczna biblioteka LibVideoGfx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LibVideoGfx library.

%description static -l pl.UTF-8
Statyczna biblioteka LibVideoGfx.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvideogfx.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/libvideogfx-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvideogfx-1.0.so.9

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libvideogfx-config
%attr(755,root,root) %{_libdir}/libvideogfx.so
%{_includedir}/libvideogfx
%{_includedir}/libvideogfx.hh
%{_pkgconfigdir}/libvideogfx.pc
%{_aclocaldir}/libvideogfx.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libvideogfx.a
%endif
