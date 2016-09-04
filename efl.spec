%ifarch %{armx}
%bcond_without opengles
%bcond_with sdl
%else
%bcond_with opengles
%bcond_without sdl
%endif
%bcond_without wayland

%define _disable_ld_no_undefined 1
%define gstapi 1.0
%define major 1


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
%define devefl %mklibname efl  -d

%define libelua %mklibname elua %{major}
%define develua %mklibname elua  -d

%define libelocation %mklibname location %{major}
%define develocation %mklibname location  -d

%define libector %mklibname ector %{major}
%define devector %mklibname ector  -d

%define libemile %mklibname emile %{major}
%define devemile %mklibname emile  -d

%define libelementary %mklibname elementary %{major}
%define develementary %mklibname elementary -d

%define devname %mklibname %{name} -d

Summary:	Enlightenment Foundation Libraries
Name:		efl
Version:	1.18.0
Release:	1
Epoch:		3
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/rel/libs/efl/%{name}-%{version}.tar.xz
Source100:      %{name}.rpmlintrc
Patch001:	fix_edje_cc_compiler_failure.patch
BuildRequires:	doxygen
BuildRequires:	gstreamer%{gstapi}-tools
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
#BuildRequires:	libjpeg-devel
#BuildRequires:	pkgconfig(libopenjpeg1)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(bullet)
BuildRequires:	pkgconfig(cairo)
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
BuildRequires:	pkgconfig(check)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(librsvg-2.0)
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
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(luajit)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(poppler-cpp)
%if %{without wayland}
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
%endif

%description
The Enlightenment Foundation Libraries are a collection of libraries
and tools upon which sophisticated graphical applications can be
built.  Included are a data structure library (Eina), a C-based object
engine (EO), a data storage library (EET), an object canvas (Evas),
and more.

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README

#----------------------------------------------------------------------------

%package -n ecore
Summary:	Enlightenment event/X abstraction layer
License:	BSD
Group:		Graphical desktop/Enlightenment

%description -n ecore
Ecore is the event/X abstraction layer that makes doing selections,
Xdnd, general X stuff, event loops, timeouts and idle handlers fast,
optimized, and convenient.

%files -n ecore
%{_bindir}/ecore_evas_convert
%{_bindir}/elua
%{_datadir}/ecore/
%{_datadir}/ecore_imf/
%{_datadir}/elua/
%{_libdir}/ecore/system/upower/*/module.so
%{_libdir}/ecore/system/systemd/*/module.so
%{_libdir}/ecore_evas/engines/*/*/module.so
%{_libdir}/ecore_imf/modules/*/*/module.so

#----------------------------------------------------------------------------

%package -n %{libecore}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	ecore = %{EVRD}

%description -n %{libecore}
Enlightenment event/X abstraction layer library.

%files -n %{libecore}
%{_libdir}/libecore.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libecore_audio}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}

%description -n %{libecore_audio}
Enlightenment event/X abstraction layer library.

%files -n %{libecore_audio}
%{_libdir}/libecore_audio.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libecore_avahi}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}

%description -n %{libecore_audio}
Enlightenment avahi abstraction layer library.

%files -n %{libecore_avahi}
%{_libdir}/libecore_avahi.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libecore_con}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}
Conflicts:	%{_lib}ecore1 < 3:1.8.0

%description -n %{libecore_con}
Enlightenment event/X abstraction layer library.

%files -n %{libecore_con}
%{_libdir}/libecore_con.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libecore_evas}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}
Conflicts:	%{_lib}ecore1 < 3:1.8.0

%description -n %{libecore_evas}
Enlightenment event/X abstraction layer library.

%files -n %{libecore_evas}
%{_libdir}/libecore_evas.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libecore_file}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}
Conflicts:	%{_lib}ecore1 < 3:1.8.0

%description -n %{libecore_file}
Enlightenment event/X abstraction layer library.

%files -n %{libecore_file}
%{_libdir}/libecore_file.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libecore_imf}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}
Conflicts:	%{_lib}ecore1 < 3:1.8.0

%description -n %{libecore_imf}
Enlightenment event/X abstraction layer library.

%files -n %{libecore_imf}
%{_libdir}/libecore_imf.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libecore_imf_evas}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}
Conflicts:	%{_lib}ecore1 < 3:1.8.0

%description -n %{libecore_imf_evas}
Enlightenment event/X abstraction layer library.

%files -n %{libecore_imf_evas}
%{_libdir}/libecore_imf_evas.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libecore_input}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}
Conflicts:	%{_lib}ecore1 < 3:1.8.0

%description -n %{libecore_input}
Enlightenment event/X abstraction layer library.

%files -n %{libecore_input}
%{_libdir}/libecore_input.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libecore_input_evas}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}
Conflicts:	%{_lib}ecore1 < 3:1.8.0

%description -n %{libecore_input_evas}
Enlightenment event/X abstraction layer library.

%files -n %{libecore_input_evas}
%{_libdir}/libecore_input_evas.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libecore_ipc}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}
Conflicts:	%{_lib}ecore1 < 3:1.8.0

%description -n %{libecore_ipc}
Enlightenment event/X abstraction layer library.

%files -n %{libecore_ipc}
%{_libdir}/libecore_ipc.so.%{major}*

#----------------------------------------------------------------------------
%if %{with sdl}
%package -n %{libecore_sdl}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}
Conflicts:	%{_lib}ecore1 < 3:1.8.0

%description -n %{libecore_sdl}
Enlightenment event/X abstraction layer library.

%files -n %{libecore_sdl}
%{_libdir}/libecore_sdl.so.%{major}*
%endif
#----------------------------------------------------------------------------

%package -n %{libecore_x}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}
Conflicts:	%{_lib}ecore1 < 3:1.8.0

%description -n %{libecore_x}
Enlightenment event/X abstraction layer library.

%files -n %{libecore_x}
%{_libdir}/libecore_x.so.%{major}*

#----------------------------------------------------------------------------
%if %{without wayland}
%package -n %{libecore_wayland}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}
Conflicts:	%{_lib}ecore1 < 3:1.8.0

%description -n %{libecore_wayland}
Enlightenment event/X abstraction layer library.

%files -n %{libecore_wayland}
%{_libdir}/libecore_wayland.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{devecore}
Summary:	Ecore headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libecore} = %{EVRD}
Requires:	%{libecore_audio} = %{EVRD}
Requires:       %{libecore_avahi} = %{EVRD}
Requires:	%{libecore_con} = %{EVRD}
Requires:	%{libecore_evas} = %{EVRD}
Requires:	%{libecore_file} = %{EVRD}
Requires:	%{libecore_imf} = %{EVRD}
Requires:	%{libecore_imf_evas} = %{EVRD}
Requires:	%{libecore_input} = %{EVRD}
Requires:	%{libecore_input_evas} = %{EVRD}
Requires:	%{libecore_ipc} = %{EVRD}
%if %{with sdl}
Requires:	%{libecore_sdl} = %{EVRD}
%endif
%if %{without wayland}
Requires:	%{libecore_wayland} = %{EVRD}
%endif
Requires:	%{libecore_x} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Provides:	ecore-devel = %{EVRD}

%description -n %{devecore}
Ecore headers and development libraries.

%files -n %{devecore}
%{_libdir}/cmake/Ecore/
%{_libdir}/cmake/EcoreCxx/
%{_libdir}/pkgconfig/ecore.pc
%{_libdir}/pkgconfig/ecore-audio.pc
%{_libdir}/pkgconfig/ecore-audio-cxx.pc
%{_libdir}/pkgconfig/ecore-avahi.pc
%{_libdir}/pkgconfig/ecore-cxx.pc
%{_libdir}/pkgconfig/ecore-con.pc
%{_libdir}/pkgconfig/ecore-evas.pc
%{_libdir}/pkgconfig/ecore-file.pc
%{_libdir}/pkgconfig/ecore-imf.pc
%{_libdir}/pkgconfig/ecore-imf-evas.pc
%{_libdir}/pkgconfig/ecore-input.pc
%{_libdir}/pkgconfig/ecore-input-evas.pc
%{_libdir}/pkgconfig/ecore-ipc.pc
%if %{with sdl}
%{_libdir}/pkgconfig/ecore-sdl.pc
%endif
%{_libdir}/pkgconfig/ecore-x.pc
%if %{without wayland}
%{_libdir}/pkgconfig/ecore-wayland.pc
%{_libdir}/pkgconfig/evas-wayland-shm.pc
%if %{with opengles}
%{_libdir}/pkgconfig/evas-wayland-egl.pc
%endif
%endif
%{_libdir}/libecore.so
%{_libdir}/libecore_audio.so
%{_libdir}/libecore_avahi.so
%{_libdir}/libecore_con.so
%{_libdir}/libecore_evas.so
%{_libdir}/libecore_file.so
%{_libdir}/libecore_imf.so
%{_libdir}/libecore_imf_evas.so
%{_libdir}/libecore_input.so
%{_libdir}/libecore_input_evas.so
%{_libdir}/libecore_ipc.so
%if %{with sdl}
%{_libdir}/libecore_sdl.so
%endif
%{_libdir}/libecore_x.so
%if %{without wayland}
%{_libdir}/libecore_wayland.so
%endif
%{_libdir}/ecore_x/bin/v-1.14/ecore_x_vsync
%{_includedir}/ecore-1/
%{_includedir}/ecore-audio-1/
%{_includedir}/ecore-audio-cxx-1/
%{_includedir}/ecore-avahi-1/
%{_includedir}/ecore-cxx-1/
%{_includedir}/ecore-con-1/
%{_includedir}/ecore-evas-1/
%{_includedir}/ecore-file-1/
%{_includedir}/ecore-imf-1/
%{_includedir}/ecore-imf-evas-1/
%{_includedir}/ecore-input-1/
%{_includedir}/ecore-input-evas-1/
%{_includedir}/ecore-ipc-1/
%if %{with sdl}
%{_includedir}/ecore-sdl-1/
%endif
%{_includedir}/ecore-x-1/
%if %{without wayland}
%{_includedir}/ecore-wayland-1/
%endif
%{_datadir}/eolian/include/ecore-1/
%{_datadir}/ecore_x/checkme

#----------------------------------------------------------------------------

%package -n edje
Summary:	Enlightenment complex graphical design and layout library extra files
License:	BSD
Group:		Graphical desktop/Enlightenment
Requires:	evas = %{EVRD}

%description -n edje
Enlightenment complex graphical design and layout library extra files.

%files -n edje
%{_bindir}/edje_*
%{_datadir}/edje/
%{_datadir}/mime/packages/edje.xml
%{_libdir}/edje/utils/*/epp

#----------------------------------------------------------------------------

%package -n %{libedje}
Summary:	Enlightenment complex graphical design and layout library
License:	BSD
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	edje = %{EVRD}

%description -n %{libedje}
Enlightenment complex graphical design and layout library for animated
resizable, compressed and scalable themes.

%files -n %{libedje}
%{_libdir}/libedje.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devedje}
Summary:	Edje headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libedje} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Provides:	edje-devel = %{EVRD}

%description -n %{devedje}
Edje headers and development libraries.

%files -n %{devedje}
%{_libdir}/cmake/Edje/
%{_libdir}/pkgconfig/edje.pc
%{_libdir}/pkgconfig/edje-cxx.pc
%{_libdir}/libedje.so
%{_includedir}/edje-1/
%{_includedir}/edje-cxx-1/
%{_datadir}/eolian/include/edje-1/

#----------------------------------------------------------------------------

%package -n eet
Summary:	Enlightenment simple compression utility
License:	BSD
Group:		Graphical desktop/Enlightenment

%description -n eet
Enlightenment simple compression utility.

%files -n eet
%{_bindir}/eet
%{_bindir}/eetpack

#----------------------------------------------------------------------------

%package -n diffeet
Summary:	Enlightenment simple compression utility
License:	BSD
Group:		Graphical desktop/Enlightenment

%description -n diffeet
Enlightenment simple compression utility.

%files -n diffeet
%{_bindir}/diffeet
%{_bindir}/vieet

#----------------------------------------------------------------------------

%package -n %{libeet}
Summary:	Enlightenment simple compression library
License:	BSD
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	eet = %{EVRD}

%description -n %{libeet}
Enlightenment simple compression library.

%files -n %{libeet}
%{_libdir}/libeet.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{deveet}
Summary:	Eet headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libeet} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Provides:	eet-devel = %{EVRD}

%description -n %{deveet}
Eet headers and development libraries.

%files -n %{deveet}
%{_libdir}/cmake/Eet/
%{_libdir}/cmake/EetCxx/
%{_libdir}/pkgconfig/eet.pc
%{_libdir}/pkgconfig/eet-cxx.pc
%{_libdir}/libeet.so
%{_includedir}/eet-1/
%{_includedir}/eet-cxx-1/

#----------------------------------------------------------------------------

%package -n eeze
Summary:	Enlightenment devices manipulation library extra files
License:	BSD
Group:		Graphical desktop/Enlightenment

%description -n eeze
Eeze is a library for manipulating devices through udev with a simple and fast
api. It interfaces directly with libudev, avoiding such middleman daemons as
udisks/upower or hal, to immediately gather device information the instant it
becomes known to the system.

%files -n eeze
%{_bindir}/eeze_disk_ls
%{_bindir}/eeze_mount
%{_bindir}/eeze_scanner
%{_bindir}/eeze_umount
%{_datadir}/eeze/
%{_libdir}/eeze/modules/

#----------------------------------------------------------------------------

%package -n %{libeeze}
Summary:	Enlightenment devices manipulation library
License:	BSD
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	eeze = %{EVRD}

%description -n %{libeeze}
Enlightenment devices manipulation library.

%files -n %{libeeze}
%{_libdir}/libeeze.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{deveeze}
Summary:	Eeze headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libeeze} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Provides:	eeze-devel = %{EVRD}

%description -n %{deveeze}
Eeze headers and development libraries.

%files -n %{deveeze}
%{_libdir}/cmake/Eeze/
%{_libdir}/pkgconfig/eeze.pc
%{_libdir}/libeeze.so
%{_includedir}/eeze-1/

#----------------------------------------------------------------------------

%package -n efreet
Summary:	Enlightenment freedesktop.org specifications implementation extra files
License:	BSD
Group:		Graphical desktop/Enlightenment
Requires(post,preun,postun):	systemd

%description -n efreet
Enlightenment freedesktop.org specifications implementation extra files.
 - Base Directory
 - Desktop Entry
 - Icon Theme
 - Menu

%files -n efreet
%{_bindir}/efreetd
%{_datadir}/efreet/
%{_datadir}/dbus-1/services/org.enlightenment.Efreet.service
%{_libdir}/efreet/*/efreet_desktop_cache_create
%{_libdir}/efreet/*/efreet_icon_cache_create
%{_userunitdir}/efreet.service

%post -n efreet
%systemd_post efreet.service

%preun -n efreet
%systemd_preun efreet.service

%postun -n efreet
%systemd_postun

#----------------------------------------------------------------------------

%package -n %{libefreet}
Summary:	Enlightenment freedesktop.org specifications implementation library
License:	BSD
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	efreet = %{EVRD}

%description -n %{libefreet}
Enlightenment freedesktop.org specifications implementation library.

%files -n %{libefreet}
%{_libdir}/libefreet.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libefreet_mime}
Summary:	Enlightenment freedesktop.org specifications implementation library
License:	BSD
Group:		System/Libraries
Requires:	%{libefreet} = %{EVRD}
Conflicts:	%{_lib}efreet1 < 2:1.8.0

%description -n %{libefreet_mime}
Enlightenment freedesktop.org specifications implementation library.

%files -n %{libefreet_mime}
%{_libdir}/libefreet_mime.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libefreet_trash}
Summary:	Enlightenment freedesktop.org specifications implementation library
License:	BSD
Group:		System/Libraries
Requires:	%{libefreet} = %{EVRD}
Conflicts:	%{_lib}efreet1 < 2:1.8.0

%description -n %{libefreet_trash}
Enlightenment freedesktop.org specifications implementation library.

%files -n %{libefreet_trash}
%{_libdir}/libefreet_trash.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devefreet}
Summary:	Efreet headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libefreet} = %{EVRD}
Requires:	%{libefreet_mime} = %{EVRD}
Requires:	%{libefreet_trash} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Provides:	efreet-devel = %{EVRD}

%description -n %{devefreet}
Efreet headers and development libraries.

%files -n %{devefreet}
%{_libdir}/cmake/Efreet/
%{_libdir}/pkgconfig/efreet.pc
%{_libdir}/pkgconfig/efreet-mime.pc
%{_libdir}/pkgconfig/efreet-trash.pc
%{_libdir}/libefreet.so
%{_libdir}/libefreet_mime.so
%{_libdir}/libefreet_trash.so
%{_includedir}/efreet-1/

#----------------------------------------------------------------------------

%package -n eina
Summary:	Enlightenment data types library extra files
License:	LGPLv2.1+
Group:		Graphical desktop/Enlightenment

%description -n eina
Enlightenment data types library extra files.

eina-bench-cmp:
- generate reports comparing two or more outputs of expedite

%files -n eina
%{_bindir}/eina-bench-cmp

#----------------------------------------------------------------------------

%package -n %{libeina}
Summary:	Enlightenment data types library
License:	LGPLv2.1+
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libeina}
Enlightenment data types library.

%files -n %{libeina}
%{_libdir}/libeina.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{deveina}
Summary:	Eina headers and development libraries
License:	LGPLv2.1+
Group:		Development/Other
Requires:	%{libeina} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Requires:	%{_lib}systemd-journal-devel
Provides:	eina-devel = %{EVRD}

%description -n %{deveina}
Eina headers and development libraries.

%files -n %{deveina}
%{_libdir}/cmake/Eina/
%{_libdir}/cmake/EinaCxx/
%{_libdir}/pkgconfig/eina.pc
%{_libdir}/pkgconfig/eina-cxx.pc
%{_libdir}/libeina.so
%{_includedir}/eina-1/
%{_includedir}/eina-cxx-1/

#----------------------------------------------------------------------------

%package -n %{libeio}
Summary:	Enlightenment Input Output library
License:	LGPLv2.1+
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libeio}
Enlightenment Input Output library.

%files -n %{libeio}
%{_libdir}/libeio.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{deveio}
Summary:	Eio headers and development libraries
License:	LGPLv2.1+
Group:		Development/Other
Requires:	%{libeio} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Provides:	eio-devel = %{EVRD}

%description -n %{deveio}
Eio headers and development libraries.

%files -n %{deveio}
%{_libdir}/pkgconfig/eio.pc
%{_libdir}/libeio.so
%{_libdir}/pkgconfig/eio-cxx.pc
%{_libdir}/cmake/Eio/
%{_includedir}/eio-cxx-1/
%{_includedir}/eio-1/
%{_datadir}/eolian/include/eio-1/


#----------------------------------------------------------------------------

%package -n eldbus
Summary:	Enlightenment dbus wrapper
License:	LGPLv2.1+
Group:		Graphical desktop/Enlightenment

%description -n eldbus
Enlightenment dbus wrapper.

%files -n eldbus
%{_bindir}/eldbus-codegen

#----------------------------------------------------------------------------

%package -n %{libeldbus}
Summary:	Enlightenment dbus wrapper library
License:	LGPLv2.1+
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	eldbus = %{EVRD}

%description -n %{libeldbus}
Enlightenment dbus wrapper library.

%files -n %{libeldbus}
%{_libdir}/libeldbus.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{develdbus}
Summary:	Eldbus headers and development libraries
License:	LGPLv2.1+
Group:		Development/Other
Requires:	%{libeldbus} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Provides:	eldbus-devel = %{EVRD}

%description -n %{develdbus}
Eldbus headers and development libraries.

%files -n %{develdbus}
%{_libdir}/cmake/Eldbus/
%{_libdir}/pkgconfig/eldbus.pc
%{_libdir}/libeldbus.so
%{_includedir}/eldbus_cxx-1/
%{_includedir}/eldbus-1/

#----------------------------------------------------------------------------

%package -n embryo
Summary:	Enlightenment bytecode virtual machine
License:	BSD
Group:		Graphical desktop/Enlightenment

%description -n embryo
Embryo is primarily a shared library that gives you an API to load and control
interpreted programs compiled into an abstract machine bytecode that it
understands. This abstract (or virtual) machine is similar to a real machine
with a CPU, but it is emulated in software.

%files -n embryo
%{_bindir}/embryo_cc
%{_datadir}/embryo/

#----------------------------------------------------------------------------

%package -n %{libembryo}
Summary:	Enlightenment bytecode virtual machine library
License:	BSD
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	embryo = %{EVRD}

%description -n %{libembryo}
Enlightenment bytecode virtual machine library.

%files -n %{libembryo}
%{_libdir}/libembryo.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devembryo}
Summary:	Embryo headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libembryo} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Provides:	embryo-devel = %{EVRD}

%description -n %{devembryo}
Embryo headers and development libraries.

%files -n %{devembryo}
%{_libdir}/pkgconfig/embryo.pc
%{_libdir}/libembryo.so
%{_includedir}/embryo-1/

#----------------------------------------------------------------------------

%package -n emotion
Summary:	Enlightenment video & media object library extra files
License:	BSD
Group:		Graphical desktop/Enlightenment

%description -n emotion
Emotion is a video & media object library designed to interface with Evas and
Ecore to provide autonomous "video" and "audio" objects that can be moved,
resized and positioned like any normal object, but instead they can play video
and audio and can be controlled from a high-level control API allowing the
programmer to quickly piece together a multi-media system with minimal work.

%files -n emotion
%{_datadir}/emotion/
%{_libdir}/emotion/
%{_libdir}/edje/modules/emotion/

#----------------------------------------------------------------------------

%package -n %{libemotion}
Summary:	Enlightenment video & media object library
License:	BSD
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	emotion = %{EVRD}

%description -n %{libemotion}
Enlightenment video & media object library.

%files -n %{libemotion}
%{_libdir}/libemotion.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devemotion}
Summary:	Emotion headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libemotion} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Provides:	emotion-devel = %{EVRD}

%description -n %{devemotion}
Emotion headers and development libraries.

%files -n %{devemotion}
%{_libdir}/cmake/Emotion/
%{_libdir}/pkgconfig/emotion.pc
%{_libdir}/libemotion.so
%{_includedir}/emotion-1/
%{_datadir}/eolian/include/emotion-1/

#----------------------------------------------------------------------------

%package -n %{libeo}
Summary:	Enlightenment generic object system library
License:	BSD
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libeo}
Enlightenment generic object system library.

%files -n %{libeo}
%{_libdir}/libeo.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{deveo}
Summary:	Eo headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libeo} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Provides:	eo-devel = %{EVRD}

%description -n %{deveo}
Eo headers and development libraries.

%files -n %{deveo}
%{_libdir}/cmake/Eo/
%{_libdir}/cmake/EoCxx/
%{_libdir}/pkgconfig/eo.pc
%{_libdir}/pkgconfig/eo-cxx.pc
%{_libdir}/libeo.so
%{_includedir}/eo-1/
%{_includedir}/eo-cxx-1/
%{_datadir}/gdb/auto-load/%{_libdir}/libeo.so.*-gdb.py
%{_datadir}/eo/gdb/eo_gdb.py
%{_datadir}/eolian/include/eo-1/

#----------------------------------------------------------------------------

%package -n eolian
Summary:	Enlightenment C++ bindings generator
License:	BSD
Group:		Graphical desktop/Enlightenment

%description -n eolian
Enlightenment C++ bindings generator.

%files -n eolian
%{_bindir}/eolian_cxx
%{_bindir}/eolian_gen

#----------------------------------------------------------------------------

%package -n %{libeolian}
Summary:	Enlightenment C++ bindings generator library
License:	BSD
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libeolian}
Enlightenment C++ bindings generator library.

%files -n %{libeolian}
%{_libdir}/libeolian.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{deveolian}
Summary:	Eolian headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libeolian} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Requires:	eolian = %{EVRD}
Provides:	eolian-devel = %{EVRD}

%description -n %{deveolian}
Eolian headers and development libraries.

%files -n %{deveolian}
%{_libdir}/cmake/Eolian/
%{_libdir}/cmake/EolianCxx/
%{_libdir}/pkgconfig/eolian.pc
%{_libdir}/pkgconfig/eolian-cxx.pc
%{_libdir}/libeolian.so
%{_includedir}/eolian-1/
%{_includedir}/eolian-cxx-1/

#----------------------------------------------------------------------------

%package -n %{libephysics}
Summary:	Enlightenment physics library
License:	BSD
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libephysics}
Ephysics is a library that manages Ecore, Evas and Bullet Physics into
an easy to use way. It's a kind of wrapper, a glue, between these libraries.
It's not intended to be a physics library (we already have many out there).

%files -n %{libephysics}
%{_libdir}/libephysics.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devephysics}
Summary:	Ephysics headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libephysics} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Provides:	ephysics-devel = %{EVRD}

%description -n %{devephysics}
Ephysics headers and development libraries.

%files -n %{devephysics}
%{_libdir}/pkgconfig/ephysics.pc
%{_libdir}/libephysics.so
%{_includedir}/ephysics-1/

#----------------------------------------------------------------------------

%package -n ethumb
Summary:	Enlightenment canvas library extra files
License:	LGPLv2.1+
Group:		Graphical desktop/Enlightenment
Requires(post,preun,postun):	systemd

%description -n ethumb
Enlightenment canvas library extra files.

Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

%files -n ethumb
%{_bindir}/ethumb
%{_bindir}/ethumbd
%{_bindir}/ethumbd_client
%{_datadir}/dbus-1/services/org.enlightenment.Ethumb.service
%{_datadir}/ethumb/
%{_datadir}/ethumb_client/
%{_libdir}/ethumb/
%{_libdir}/ethumb_client/
%{_userunitdir}/ethumb.service

%post -n ethumb
%systemd_post ethumb.service

%preun -n ethumb
%systemd_preun ethumb.service

%postun -n ethumb
%systemd_postun

#----------------------------------------------------------------------------

%package -n %{libethumb}
Summary:	Enlightenment thumbnailing library
License:	LGPLv2.1+
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	ethumb = %{EVRD}

%description -n %{libethumb}
Enlightenment thumbnailing library.

%files -n %{libethumb}
%{_libdir}/libethumb.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libethumb_client}
Summary:	Enlightenment thumbnailing library
License:	LGPLv2.1+
Group:		System/Libraries
Requires:	%{libethumb} = %{EVRD}
Conflicts:	%{_lib}ethumb1 < 1.7.9

%description -n %{libethumb_client}
Enlightenment thumbnailing library.

%files -n %{libethumb_client}
%{_libdir}/libethumb_client.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devethumb}
Summary:	Ethumb headers and development libraries
License:	LGPLv2.1+
Group:		Development/Other
Requires:	%{libethumb} = %{EVRD}
Requires:	%{libethumb_client} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Provides:	ethumb-devel = %{EVRD}

%description -n %{devethumb}
Ethumb headers and development libraries.

%files -n %{devethumb}
%{_libdir}/cmake/Ethumb/
%{_libdir}/cmake/EthumbClient/
%{_libdir}/pkgconfig/ethumb.pc
%{_libdir}/pkgconfig/ethumb_client.pc
%{_libdir}/libethumb.so
%{_libdir}/libethumb_client.so
%{_includedir}/ethumb-1/
%{_includedir}/ethumb-client-1/

#----------------------------------------------------------------------------

%package -n evas
Summary:	Enlightenment canvas library extra files
License:	BSD
Group:		Graphical desktop/Enlightenment

%description -n evas
Enlightenment canvas library extra files.

Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

%files -n evas
%{_bindir}/evas_cserve2_client
%{_bindir}/evas_cserve2_debug
%{_bindir}/evas_cserve2_shm_debug
%{_bindir}/evas_cserve2_usage
%{_datadir}/evas/
%{_libdir}/evas/modules/engines/*/*/*.so
%{_libdir}/evas/modules/image_loaders/*/*/*.so
%{_libdir}/evas/modules/utils/evas_image_loader.*
%{_libdir}/evas/modules/image_savers/*/*/*.so
%{_libdir}/evas/cserve2/bin/*/evas_cserve2
%{_libdir}/evas/cserve2/bin/*/evas_cserve2_slave

#----------------------------------------------------------------------------

%package -n %{libevas}
Summary:	Enlightenment canvas library
License:	BSD
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	evas = %{EVRD}

%description -n %{libevas}
Enlightenment canvas library.

%files -n %{libevas}
%{_libdir}/libevas.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devevas}
Summary:	Evas headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libevas} = %{EVRD}
Requires:	%{devefl} = %{EVRD}
Provides:	evas-devel = %{EVRD}

%description -n %{devevas}
Evas headers and development libraries.

%files -n %{devevas}
%{_libdir}/cmake/Evas/
%{_libdir}/cmake/EvasCxx/
%{_libdir}/pkgconfig/evas.pc
%{_libdir}/pkgconfig/evas-cxx.pc
%if %{with sdl}
%{_libdir}/pkgconfig/evas-opengl-sdl.pc
%endif
%{_libdir}/pkgconfig/evas-opengl-x11.pc
%{_libdir}/pkgconfig/evas-software-buffer.pc
%{_libdir}/pkgconfig/evas-software-x11.pc
%{_libdir}/libevas.so
%{_includedir}/evas-1/
%{_includedir}/evas-cxx-1/
%{_datadir}/eolian/include/evas-1/

#----------------------------------------------------------------------------

%package -n %{libefl}
Summary:	Enlightenment canvas library
License:	BSD
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libefl}
Enlightenment canvas library.

%files -n %{libefl}
%{_libdir}/libefl.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devefl}
Summary:	EFL headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libefl} = %{EVRD}
Provides:	efl-devel = %{EVRD}

%description -n %{devefl}
EFL headers and development libraries.

%files -n %{devefl}
%{_libdir}/pkgconfig/efl.pc
%{_libdir}/pkgconfig/efl-cxx.pc
%{_libdir}/libefl.so
%{_datadir}/eolian/include/efl-1/
%{_includedir}/%{name}-cxx-1/*.hh
%{_includedir}/%{name}-1/interfaces/*.h
%{_libdir}/cmake/Efl/

#----------------------------------------------------------------------------

%package -n %{libelua}
Summary:        Support Library for lua scripts
License:        BSD
Group:          System/Libraries
Requires:       %{name} = %{EVRD}

%description -n %{libelua}
Lua support library

%files -n %{libelua}
%{_libdir}/libelua.so.%{major}*

#----------------------------------------------------------------------------
%package -n %{develua}
Summary:	Elua headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libelua} = %{EVRD}
Requires:	%{develua} = %{EVRD}

%description -n %{develua}
elua headers and development libraries.

%files -n %{develua}
%{_libdir}/libelua.so
%{_libdir}/pkgconfig/elua.pc
%{_includedir}/elua-1/
%{_libdir}/cmake/Elua/

#----------------------------------------------------------------------------
%package -n %{libelocation}
Summary:        Enlightenment geolocation libraries
License:        BSD
Group:          System/Libraries
Requires:       %{name} = %{EVRD}

%description -n %{libelocation}
Enlightenment geolocation libraries

%files -n %{libelocation}
%{_libdir}/libelocation.so.%{major}*

#----------------------------------------------------------------------------
%package -n %{develocation}
Summary:	Elocation headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libelocation} = %{EVRD}
Requires:	%{develocation} = %{EVRD}

%description -n %{develocation}
elocation headers and development libraries.

%files -n %{develocation}
%{_libdir}/libelocation.so
%{_libdir}/pkgconfig/elocation.pc
%{_includedir}/elocation-1/

%package -n %{libector}
Summary:        Enlightenment rendering libraries
License:        BSD
Group:          System/Libraries
Requires:       %{name} = %{EVRD}

%description -n %{libector}
Enlightenment rendering libraries

%files -n %{libector}
%{_libdir}/libector.so.%{major}*

#----------------------------------------------------------------------------
%package -n %{devector}
Summary:	Ector headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libector} = %{EVRD}
Requires:	%{devector} = %{EVRD}

%description -n %{devector}
ector headers and development libraries.

%files -n %{devector}
%{_libdir}/libector.so
%{_libdir}/pkgconfig/ector.pc
%{_includedir}/ector-1/
%{_datadir}/eolian/include/ector-1/


%package -n %{libemile}
Summary:        Enlightenment encoding libraries
License:        BSD
Group:          System/Libraries
Requires:       %{name} = %{EVRD}

%description -n %{libemile}
Enlightenment encoding libraries

%files -n %{libemile}
%{_libdir}/libemile.so.%{major}*

#----------------------------------------------------------------------------
%package -n %{devemile}
Summary:	Emile headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libemile} = %{EVRD}
Requires:	%{devemile} = %{EVRD}

%description -n %{devemile}
emile headers and development libraries.

%files -n %{devemile}
%{_libdir}/libemile.so
%{_libdir}/pkgconfig/emile.pc
%{_libdir}/cmake/Emile/
%{_includedir}/emile-1/
#----------------------------------------------------------------------------
%package -n elementary 
Summary:	Basic widget set based on EFL for mobile touch-screen devices
#Name:		elementary
#Version:	1.18.0
#Release:	0
License:	LGPLv2.1+
Group:		Graphical desktop/Enlightenment
#Url:		http://www.enlightenment.org/

%description
A basic widget set that is easy to use based on EFL for mobile
touch-screen devices.

This package is part of the Enlightenment DR18 desktop shell.

%files -n elementary
%doc AUTHORS COPYING README
%{_bindir}/%{name}_run
%{_bindir}/elementary_codegen
%{_bindir}/elementary_config
%{_bindir}/elementary_quicklaunch
%{_bindir}/elm_prefs_cc
%{_libdir}/edje/modules/elm/v*/module.so
%{_libdir}/elementary/modules/access_output/v*
%{_libdir}/elementary/modules/prefs/v*
%{_datadir}/applications/%{name}_config.desktop
%{_datadir}/%{name}/config/*
%{_datadir}/%{name}/edje_externals/*
%{_datadir}/%{name}/images/*
%{_datadir}/%{name}/themes/default.edj
%{_datadir}/%{name}/objects/*
%{_iconsdir}/%{name}.png

#----------------------------------------------------------------------------

%package -n %{libelementary}
Summary:	Libraries for the %{name} package
Group:		System/Libraries

%description -n %{libelementary}
Libraries for %{libelementary}.

%files -n %{libelementary}
%{_libdir}/libelementary.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{develementary}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develementary}
elementary development headers and libraries.

%files -n %{develementary}
%{_bindir}/elementary_test
%{_libdir}/cmake/Elementary/
%{_libdir}/pkgconfig/elementary.pc
%{_libdir}/pkgconfig/elementary-cxx.pc
#%{_libdir}/*.so
%{_libdir}/libelementary.so.%{major}*
%{_libdir}/elementary/modules/test_entry/v*
%{_libdir}/elementary/modules/test_map/v*
%{_libdir}/elementary/modules/datetime_input_ctxpopup/v*
%{_datadir}/applications/%{name}_test.desktop
%{_datadir}/eolian/include/elementary-1/*.eo
%{_includedir}/elementary-1/*
%{_includedir}/elementary-cxx*


%prep
%setup -q
#%apply_patches
patch -p0 < fix_edje_cc_compiler_failure.patch

%build
autoreconf -vif 
%configure2_5x \
	--enable-fontconfig \
	--enable-gstreamer-1.0 \
	--enable-image-loader-bmp \
	--enable-image-loader-eet \
	--enable-image-loader-generic \
	--enable-image-loader-gif \
	--enable-image-loader-ico \
	--enable-image-loader-jpeg \
	--enable-image-loader-jp2k \
	--enable-image-loader-pmaps \
	--enable-image-loader-png \
	--enable-image-loader-psd \
	--enable-image-loader-tga \
	--enable-image-loader-tiff \
	--enable-image-loader-wbmp \
	--enable-image-loader-webp \
	--enable-image-loader-xpm \
%if %{with sdl}
	--enable-sdl \
%endif
%if %{with opengles}
	--with-opengl=es \
%endif
%if %{without wayland}
	--enable-wayland \
	--enable-egl \
%endif
	--enable-systemd \
	--enable-v4l2 \
	--enable-xine \
	--enable-harfbuzz \
	--with-eject \
	--with-mount \
	--with-umount \
	--disable-static \
	--with-pic=evas \
	--with-pic=eina \
	--disable-poppler \

%make 

%install
%makeinstall_std

%find_lang %{name}
