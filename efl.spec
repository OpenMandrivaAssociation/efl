%global optflags %{optflags} -O2

%ifarch %{armx}
%bcond_without opengles
%bcond_without sdl
%else
%bcond_without opengles
%bcond_without sdl
%endif

%bcond_without wayland


%define _disable_ld_no_undefined 1
%define gstapi 1.0
%define major 1

%define libname %mklibname %{name} %major
%define devname %mklibname %{name} -d

%define shortver 1.25

Summary:	Enlightenment Foundation Libraries
Name:		efl
Version:	1.26.1
Release:	1
Epoch:		3
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/rel/libs/efl/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
Patch0:		fix_edje_cc_compile_failure.patch
BuildRequires: meson
BuildRequires: doxygen
BuildRequires: gstreamer%{gstapi}-tools
BuildRequires: gettext-devel
BuildRequires: giflib-devel
BuildRequires: jpeg-devel
BuildRequires: libraw-devel
BuildRequires: psiconv-devel
BuildRequires: egl-devel
BuildRequires: pkgconfig(libavif)
BuildRequires: pkgconfig(avahi-core)
BuildRequires: pkgconfig(avahi-client)
BuildRequires: pkgconfig(bullet)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(check)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(gstreamer-%{gstapi})
BuildRequires: pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires: pkgconfig(gstreamer-video-%{gstapi})
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(libcares)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libxine)
BuildRequires: pkgconfig(lua)
BuildRequires: pkgconfig(mount)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(scim)
%if %{with sdl}
BuildRequires: pkgconfig(sdl2)
%endif
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xp)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xpm)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(luajit)
BuildRequires: pkgconfig(lua)
BuildRequires: pkgconfig(rlottie)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(poppler-cpp)
BuildRequires: pkgconfig(libspectre)
BuildRequires: pkgconfig(printproto)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libinput)
Buildrequires: pkgconfig(libudev)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: vlan-utils
%if %{with wayland}
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: wayland-protocols-devel
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: wayland-tools
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(libglvnd)
%endif

Requires:  %{libname} = %{EVRD}

%define        obsversion       1.25.1
%define        obsrelease       3

Obsoletes: libecore                < %{obsversion}-%{obsrelease}
Obsoletes: libecore_audio          < %{obsversion}-%{obsrelease}
Obsoletes: libecore_avahi          < %{obsversion}-%{obsrelease}
Obsoletes: libecore_con            < %{obsversion}-%{obsrelease}
Obsoletes: libecore_evas           < %{obsversion}-%{obsrelease}
Obsoletes: libecore_file           < %{obsversion}-%{obsrelease}
Obsoletes: libecore_imf            < %{obsversion}-%{obsrelease}
Obsoletes: libecore_imf_evas       < %{obsversion}-%{obsrelease}
Obsoletes: libecore_input          < %{obsversion}-%{obsrelease}
Obsoletes: libecore_input_evas     < %{obsversion}-%{obsrelease}
Obsoletes: libecore_ipc            < %{obsversion}-%{obsrelease}
Obsoletes: libecore_sdl < %{obsversion}-%{obsrelease}
Obsoletes: libecore_x < %{obsversion}-%{obsrelease}
Obsoletes: libecore_wayland < %{obsversion}-%{obsrelease}
Obsoletes: libecore_wl2 < %{obsversion}-%{obsrelease}
Obsoletes: devecore < %{obsversion}-%{obsrelease}
Obsoletes: libedje < %{obsversion}-%{obsrelease}
Obsoletes: devedje < %{obsversion}-%{obsrelease}
Obsoletes: libeet < %{obsversion}-%{obsrelease}
Obsoletes: deveet < %{obsversion}-%{obsrelease}
Obsoletes: libeeze < %{obsversion}-%{obsrelease}
Obsoletes: deveeze < %{obsversion}-%{obsrelease}
Obsoletes: libefreet < %{obsversion}-%{obsrelease}
Obsoletes: libefreet_mime < %{obsversion}-%{obsrelease}
Obsoletes: libefreet_trash < %{obsversion}-%{obsrelease}
Obsoletes: devefreet < %{obsversion}-%{obsrelease}
Obsoletes: libeina < %{obsversion}-%{obsrelease}
Obsoletes: deveina < %{obsversion}-%{obsrelease}
Obsoletes: libeio < %{obsversion}-%{obsrelease}
Obsoletes: deveio < %{obsversion}-%{obsrelease}
Obsoletes: libeldbus < %{obsversion}-%{obsrelease}
Obsoletes: develdbus < %{obsversion}-%{obsrelease}
Obsoletes: libembryo < %{obsversion}-%{obsrelease}
Obsoletes: devembryo < %{obsversion}-%{obsrelease}
Obsoletes: libemotion < %{obsversion}-%{obsrelease}
Obsoletes: devemotion < %{obsversion}-%{obsrelease}
Obsoletes: libeo < %{obsversion}-%{obsrelease}
Obsoletes: deveo < %{obsversion}-%{obsrelease}
Obsoletes: deveo_dbg < %{obsversion}-%{obsrelease}
Obsoletes: libeolian < %{obsversion}-%{obsrelease}
Obsoletes: deveolian < %{obsversion}-%{obsrelease}
Obsoletes: libephysics < %{obsversion}-%{obsrelease}
Obsoletes: devephysics < %{obsversion}-%{obsrelease}
Obsoletes: libethumb < %{obsversion}-%{obsrelease}
Obsoletes: libethumb_client < %{obsversion}-%{obsrelease}
Obsoletes: devethumb < %{obsversion}-%{obsrelease}
Obsoletes: libevas < %{obsversion}-%{obsrelease}
Obsoletes: devevas < %{obsversion}-%{obsrelease}
Obsoletes: libefl < %{obsversion}-%{obsrelease}
Obsoletes: devefl < %{obsversion}-%{obsrelease}
Obsoletes: libefl_wl < %{obsversion}-%{obsrelease}
Obsoletes: devefl_wl < %{obsversion}-%{obsrelease}
Obsoletes: libemile < %{obsversion}-%{obsrelease}
Obsoletes: devemile < %{obsversion}-%{obsrelease}
Obsoletes: libector < %{obsversion}-%{obsrelease}
Obsoletes: devector < %{obsversion}-%{obsrelease}
Obsoletes: libelua < %{obsversion}-%{obsrelease}
Obsoletes: develua < %{obsversion}-%{obsrelease}
Obsoletes: libelocation < %{obsversion}-%{obsrelease}
Obsoletes: develocation < %{obsversion}-%{obsrelease}
Obsoletes: libelementary < %{obsversion}-%{obsrelease}
Obsoletes: develementary < %{obsversion}-%{obsrelease}
Obsoletes: libel < %{obsversion}-%{obsrelease}
Obsoletes: devel < %{obsversion}-%{obsrelease}
Obsoletes: libelput < %{obsversion}-%{obsrelease}
Obsoletes: develput < %{obsversion}-%{obsrelease}
Obsoletes: libefl_canvas_wl < %{obsversion}-%{obsrelease}
Obsoletes: devefl_canvas_wl < %{obsversion}-%{obsrelease}
Obsoletes: libexactness < %{obsversion}-%{obsrelease}
Obsoletes: devexactness < %{obsversion}-%{obsrelease}

%description
The Enlightenment Foundation Libraries are a collection of libraries
and tools upon which sophisticated graphical applications can be
built.  Included are a data structure library (Eina), a C-based object
engine (EO), a data storage library (EET), an object canvas (Evas),
and more.

#----------------------------------------------------------------------------

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_datadir}/dbus-1
%{_datadir}/ecore
%{_datadir}/ecore_imf
%{_datadir}/ecore_x
%{_datadir}/edje
%{_datadir}/eeze
%{_datadir}/efreet
%{_datadir}/elua
%{_datadir}/embryo
%{_datadir}/emotion
%{_datadir}/eo
%{_datadir}/ethumb
%{_datadir}/ethumb_client
%{_datadir}/evas
%{_datadir}/gdb/auto-load/usr/lib/*
%{_datadir}/mime/packages/edje.xml
%{_datadir}/eolian
%{_datadir}/exactness
%dir %{_datadir}/elementary
%{_datadir}/elementary/config
%{_datadir}/elementary/edje_externals
%{_datadir}/elementary/images
%{_datadir}/elementary/objects
%{_datadir}/elementary/test*
%dir %{_datadir}/elementary/themes
%{_datadir}/elementary/themes/default.edj
%{_datadir}/elementary/colors*
%{_datadir}/applications
%{_datadir}/mime/packages/evas.xml
%{_iconsdir}/Enlightenment-X
%{_iconsdir}/hicolor/128x128/apps/elementary.png
%{_libdir}/ecore*
%{_libdir}/edje
%{_libdir}/eeze
%{_libdir}/efreet
%{_libdir}/emotion
%{_libdir}/ethumb
%{_libdir}/ethumb_client
%{_libdir}/evas
%{_libdir}/elementary
%{_userunitdir}/*.service

#----------------------------------------------------------------------------

%package -n %{libname}
Summary: Libraries for the %{name} package
Group: System/Libraries

%description -n %{libname}
Libraries for %{name}.

%files -n %{libname}
%doc AUTHORS README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

#----------------------------------------------------------------------------
%package -n %{devname}
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires:  %{libname} = %{EVRD}
Provides:  %{name}-devel = %{EVRD}

%description -n %{devname}
%{name} development headers and libraries.

%files -n %{devname}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/cmake/*

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1
%build

%meson \
       -Dxinput22=true \
       -Dsystemd=true \
       -Dharfbuzz=true \
       -Dsdl=true \
       -Decore-imf-loaders-disabler='ibus,scim' \
       -Devas-loaders-disabler='json,heif' \
       -Dfb=true \
       -Dwl=true \
       -Ddrm=true \
       -Dopengl=es-egl \
       -Dinstall-eo-files=true \
       -Dbindings=cxx
#If we want wayland support then OpenGL full need to be disabled, we need to use gles.
#       -Dopengl=full

%meson_build

%install

%meson_install

%find_lang %{name}
