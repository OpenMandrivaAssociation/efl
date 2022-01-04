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

%define libecore %mklibname ecore %{major}
%define libecore_audio %mklibname ecore_audio %{major}
%define libecore_avahi %mklibname ecore_avahi %{major}
%define libecore_con %mklibname ecore_con %{major}
%define libecore_evas %mklibname ecore_evas %{major}
%define libecore_file %mklibname ecore_file %{major}
%define libecore_imf %mklibname ecore_imf %{major}
%define libecore_imf_evas %mklibname ecore_imf_evas %{major}
%define libecore_input %mklibname ecore_input %{major}
%define libecore_input_evas %mklibname ecore_input_evas %{major}
%define libecore_ipc %mklibname ecore_ipc %{major}
%define libecore_sdl %mklibname ecore_sdl %{major}
%define libecore_x %mklibname ecore_x %{major}
%define libecore_wayland %mklibname ecore_wayland %{major}
%define libecore_wl2 %mklibname ecore_wl2 %{major}
%define devecore %mklibname ecore -d

%define libedje %mklibname edje %{major}
%define devedje %mklibname edje -d

%define libeet %mklibname eet %{major}
%define deveet %mklibname eet -d

%define libeeze %mklibname eeze %{major}
%define deveeze %mklibname eeze -d

%define libefreet %mklibname efreet %{major}
%define libefreet_mime %mklibname efreet_mime %{major}
%define libefreet_trash %mklibname efreet_trash %{major}
%define devefreet %mklibname efreet -d

%define libeina %mklibname eina %{major}
%define deveina %mklibname eina -d

%define libeio %mklibname eio %{major}
%define deveio %mklibname eio -d

%define libeldbus %mklibname eldbus %{major}
%define develdbus %mklibname eldbus -d

%define libembryo %mklibname embryo %{major}
%define devembryo %mklibname embryo -d

%define libemotion %mklibname emotion %{major}
%define devemotion %mklibname emotion -d

%define libeo %mklibname eo %{major}
%define deveo %mklibname eo -d
#%%define deveo_dbg %%mklibname deveo_dbg -d

%define libeolian %mklibname eolian %{major}
%define deveolian %mklibname eolian -d

%define libephysics %mklibname ephysics %{major}
%define devephysics %mklibname ephysics -d

%define libethumb %mklibname ethumb %{major}
%define libethumb_client %mklibname ethumb_client %{major}
%define devethumb %mklibname ethumb -d

%define libevas %mklibname evas %{major}
%define devevas %mklibname evas -d

%define libefl %mklibname efl %{major}
%define devefl %mklibname efl -d

%define libefl_wl %mklibname efl_wl %{major}
%define devefl_wl %mklibname efl_wl -d

%define libemile %mklibname emile %{major}
%define devemile %mklibname emile  -d

%define libector %mklibname ector %{major}
%define devector %mklibname ector -d

%define libelua %mklibname elua %{major}
%define develua %mklibname elua -d

%define libelocation %mklibname location %{major}
%define develocation %mklibname location -d

%define libelementary %mklibname elementary %{major}
%define develementary %mklibname elementary -d

%define libel %mklibname el %{major}
%define devel %mklibname el -d

%define libelput %mklibname elput %{major}
%define develput %mklibname elput -d

%define libefl_canvas_wl %mklibname efl_canvas_wl %{major}
%define devefl_canvas_wl %mklibname efl_canvas_wl -d

%define libexactness %mklibname exactness %{major}
%define devexactness %mklibname exactness -d

%define shortver 1.25

Summary:	Enlightenment Foundation Libraries
Name:		efl
Version:	1.26.0
Release:	1
Epoch:		3
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/rel/libs/efl/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
Patch0:		fix_edje_cc_compile_failure.patch
BuildRequires: meson
BuildRequires:	doxygen
BuildRequires:	gstreamer%{gstapi}-tools
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	jpeg-devel
BuildRequires:	libraw-devel
BuildRequires: psiconv-devel
BuildRequires: egl-devel
#BuildRequires: pkgconfig(libavif)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(bullet)
BuildRequires:	pkgconfig(cairo)
BuildRequires: pkgconfig(check)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-video-%{gstapi})
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libcares)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(mount)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(scim)
%if %{with sdl}
BuildRequires:	pkgconfig(sdl2)
%endif
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xp)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xtst)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(luajit)
BuildRequires: pkgconfig(lua)
BuildRequires: pkgconfig(rlottie)
BuildRequires: pkgconfig(gbm)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	pkgconfig(poppler-cpp)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(printproto)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libinput)
Buildrequires:	pkgconfig(libudev)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  vlan-utils
%if %{with wayland}
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	wayland-protocols-devel
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	wayland-tools
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(libglvnd)
%endif

Requires:  %{libname} = %{version}-%{release}

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
%{_datadir}/applications
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
Requires:  %{libname} = %{version}-%{release}
Provides:  %{name}-devel = %{version}-%{release}

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
