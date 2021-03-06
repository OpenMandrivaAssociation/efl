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
Version:	1.25.1
Release:	2
Epoch:		3
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/rel/libs/efl/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
Patch0:		fix_edje_cc_compile_failure.patch
#Patch01:	fix-poppler-cpp-pic-level-failure.patch
#Patch02:	fix-inline-assembler.patch
#Patch03:        cmake-extra-else-fix.patch
#Patch04:  efl-1.23.1-luajitfix.patch
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

%description
The Enlightenment Foundation Libraries are a collection of libraries
and tools upon which sophisticated graphical applications can be
built.  Included are a data structure library (Eina), a C-based object
engine (EO), a data storage library (EET), an object canvas (Evas),
and more.

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/efl_debug
%{_bindir}/efl_debugd

#%{_bindir}/efl_wl_test
#%{_bindir}/efl_wl_test_stack

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
#{_bindir}/elua
%{_datadir}/ecore/
%{_datadir}/ecore_imf/
%{_datadir}/elua/
%{_libdir}/ecore/system/upower/*/module.so
%{_libdir}/ecore/system/systemd/*/module.so
%{_libdir}/ecore_evas/engines/*/*/module.so
%{_libdir}/ecore_imf/modules/*/*/module.so
%{_libdir}/ecore_con/utils/*/efl_net_proxy_helper

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
%{_libdir}/libecore_drm2.so.%{major}*
%{_libdir}/libecore_fb.so.%{major}*

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

%description -n %{libecore_avahi}
Enlightenment avahi abstraction layer library.

%files -n %{libecore_avahi}
#%{_libdir}/libecore_avahi.so.%{major}*

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
%{_libdir}/libecore_sdl.so*
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

%package -n %{libecore_wl2}
Summary:	Enlightenment event/X abstraction layer library
License:	BSD
Group:		System/Libraries
Requires:	%{libecore} = %{EVRD}
Conflicts:	%{_lib}ecore1 < 3:1.8.0

%description -n %{libecore_wl2}
Enlightenment event/X abstraction layer library.

%files -n %{libecore_wl2}
%{_libdir}/libecore_wl2.so.%{major}*
%{_libdir}/ecore_wl2/engines/dmabuf/v-%{shortver}/module.so

#----------------------------------------------------------------------------

%package -n %{devecore}
Summary:	Ecore headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libecore} = %{EVRD}
Requires:	%{libecore_audio} = %{EVRD}
Requires:	%{libecore_avahi} = %{EVRD}
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
#{_libdir}/pkgconfig/ecore-audio-cxx.pc
#%{_libdir}/pkgconfig/ecore-avahi.pc
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
#%%if %%{without wayland}
#{_libdir}/pkgconfig/evas-wayland-shm.pc
#%%endif
#%if %{with opengles}
#{_libdir}/pkgconfig/evas-wayland-egl.pc
#endif
%{_libdir}/pkgconfig/ecore-wl2.pc
%{_libdir}/libecore.so
%{_libdir}/libecore_audio.so
#%{_libdir}/libecore_avahi.so
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
%{_libdir}/libecore_wl2.so
%{_libdir}/libecore_drm2.so
%{_libdir}/libecore_fb.so
#%%{_libdir}/ecore_wl2/engines/dmabuf/v-%%{shortver}/*.debug
%{_includedir}/ecore-1/
%{_includedir}/ecore-audio-1/
#%{_includedir}/ecore-avahi-1/
%{_includedir}/ecore-cxx-1/
%{_includedir}/ecore-con-1/
%{_includedir}/ecore-evas-1/
%{_includedir}/ecore-file-1/
%{_includedir}/ecore-imf-1/
%{_includedir}/ecore-imf-evas-1/
%{_includedir}/ecore-input-1/
%{_includedir}/ecore-input-evas-1/
%{_includedir}/ecore-ipc-1/
%{_includedir}/ecore-wl2-1/
%{_includedir}/ecore-drm2-1/Ecore_Drm2.h
%{_includedir}/ecore-fb-1/Ecore_Fb.h
%{_libdir}/pkgconfig/ecore-drm2.pc
%{_libdir}/pkgconfig/ecore-fb.pc
%if %{with sdl}
%{_includedir}/ecore-sdl-1/
%endif
%{_includedir}/ecore-x-1/
%if %{without wayland}
%{_includedir}/ecore-wayland-1/
%endif
%{_datadir}/eolian/include/ecore-1/
#{_datadir}/eolian/include/eldbus-1/
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
%{_libdir}/edje/modules/elm/v*/module.so

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
%{_bindir}/eeze_scanner_monitor
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
%{_libdir}/efreet/*/efreet_desktop_cache_create
%{_libdir}/efreet/*/efreet_icon_cache_create
%{_libdir}/efreet/*/efreet_mime_cache_create

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
#{_bindir}/eina-bench-cmp
%{_bindir}/eina_btlog
%{_bindir}/eina_modinfo

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
%{_libdir}/pkgconfig/eio-cxx.pc
%{_libdir}/cmake/Eio/
%{_libdir}/libeio.so
#{_datadir}/eolian/include/eio-1/eio_model.eo
%{_datadir}/eolian/include/eio-1/eio_sentry.eo
%{_includedir}/eio-1/
%{_includedir}/eio-cxx-1/

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
%{_libdir}/pkgconfig/eldbus-cxx.pc
%{_libdir}/libeldbus.so
%{_includedir}/eldbus-cxx-1/*
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
%{_bindir}/emotion_test*
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

%package -n 	%{libeo}
Summary:	Enlightenment generic object system library
License:	BSD
Group:		System/Libraries
Requires:	%{libeo} = %{EVRD}

%description -n %{libeo}
Enlightenment generic object system library.

%files -n %{libeo}
%{_libdir}/libeo.so.%{major}*

#----------------------------------------------------------------------------

#%%package -n     %{deveo_dbg}
#Summary:        Eo debug libraries
#License:        BSD
#Group:          Development/Other
#Requires:       %%{deveo} = %%{EVRD}
#Provides:       %%{deveo_dbg} = %%{EVRD}

#%%description -n %%{deveo_dbg}
#Eo debug libraries.

#%%files -n %%{deveo_dbg}
#%%{_libdir}/libeo_dbg.so.%%{major}*
#%%{_libdir}/libeo_dbg.so

#----------------------------------------------------------------------------

%package -n 	%{deveo}
Summary:	Eo headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libeo} = %{EVRD}
Provides:	%{deveo} = %{EVRD}

%description -n %{deveo}
Eo headers and development libraries.

%files -n %{deveo}
%{_bindir}/eo_debug
%{_libdir}/cmake/Eo/
%{_libdir}/cmake/EoCxx/
%{_libdir}/pkgconfig/eo.pc
%{_libdir}/pkgconfig/eo-cxx.pc
%{_includedir}/eo-1/
%{_includedir}/eo-cxx-1/
#{_datadir}/gdb/auto-load/%{_libdir}/libeo.so.*-gdb.py
%{_datadir}/eo/gdb/eo_gdb.py
%{_datadir}/eolian/include/eo-1/
%{_libdir}/libeo.so
%{_libdir}/libeo_dbg.so.%{major}*
%{_libdir}/libeo_dbg.so
%{_datadir}/gdb/auto-load/usr/lib/libeo.so*
%ifnarch %{arm} %{armx}
#%{_datadir}/eo/gdb/__pycache__/*.pyc
#%{_datadir}/gdb/auto-load/usr/lib/__pycache__/libeo.so*
%endif
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
%{_datadir}/eolian/include/eio-1/efl_io_manager.eo
%{_datadir}/eolian/include/eio-1/efl_io_model.eo

#----------------------------------------------------------------------------

#package -n %{libephysics}
#Summary:	Enlightenment physics library
#License:	BSD
#Group:		System/Libraries
#Requires:	%{name} = %{EVRD}
#
#description -n %{libephysics}
#Ephysics is a library that manages Ecore, Evas and Bullet Physics into
#an easy to use way. It's a kind of wrapper, a glue, between these libraries.
#It's not intended to be a physics library (we already have many out there).
#
#files -n %{libephysics}
#{_libdir}/libephysics.so.%{major}*

#----------------------------------------------------------------------------

#package -n %{devephysics}
#Summary:	Ephysics headers and development libraries
#License:	BSD
#Group:		Development/Other
#Requires:	%{libephysics} = %{EVRD}
#Requires:	%{devefl} = %{EVRD}
#Provides:	ephysics-devel = %{EVRD}
#
#description -n %{devephysics}
#Ephysics headers and development libraries.
#
#files -n %{devephysics}
#{_libdir}/pkgconfig/ephysics.pc
#{_libdir}/libephysics.so
#{_includedir}/ephysics-1/

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
%{_libdir}/pkgconfig/ethumb-client.pc
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
#{_bindir}/evas_cserve2_client
#{_bindir}/evas_cserve2_debug
#{_bindir}/evas_cserve2_shm_debug
#{_bindir}/evas_cserve2_usage
%{_datadir}/evas/
%{_libdir}/evas/modules/engines/*/*/*.so
#{_libdir}/evas/modules/image_loaders/*/*/*.so
#{_libdir}/evas/utils/evas_generic_pdf_loader.*
%{_libdir}/evas/modules/image_loaders/*/v-%{shortver}/module.so
%{_libdir}/evas/modules/image_savers/*/v-%{shortver}/module.so
#{_libdir}/evas/modules/image_savers/*/*/*.so
%{_libdir}/evas/utils/evas_image_loader.*
%{_libdir}/evas/utils/evas_generic_pdf_loader*
#{_libdir}/evas/cserve2/bin/*/evas_cserve2
#{_libdir}/evas/cserve2/bin/*/evas_cserve2_slave

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
#{_libdir}/pkgconfig/evas-opengl-sdl.pc
#{_libdir}/pkgconfig/evas-opengl-x11.pc
#{_libdir}/pkgconfig/evas-software-buffer.pc
#{_libdir}/pkgconfig/evas-software-x11.pc
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
%{_libdir}/pkgconfig/efl-core.pc
%{_libdir}/pkgconfig/efl-net.pc
%{_libdir}/pkgconfig/efl-ui.pc
%{_libdir}/libefl.so
%{_datadir}/eolian/include/efl-1/
%{_includedir}/%{name}-cxx-1/
%{_includedir}/%{name}-1/
%{_libdir}/cmake/Efl/
%{_libdir}/cmake/Elua/

#----------------------------------------------------------------------------
%package -n %{libefl_wl}
Summary:        Enlightenment canvas library Wayland
License:        BSD
Group:          System/Libraries
Requires:       %{name} = %{EVRD}

%description -n %{libefl_wl}
Enlightenment canvas library for wayland.

%files -n %{libefl_wl}
#%{_libdir}/libefl_wl.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devefl_wl}
Summary:        EFL Wayland headers and development libraries
License:        BSD
Group:          Development/Other
Requires:       %{libefl_wl} = %{EVRD}
Provides:       efl_wl-devel = %{EVRD}

%description -n %{devefl_wl}
EFL Wayland headers and development libraries.

%files -n %{devefl_wl}
#%{_bindir}/efl_wl_test
#%{_bindir}/efl_wl_test_stack
#%{_libdir}/pkgconfig/efl-wl.pc
%{_libdir}/pkgconfig/efl-cxx.pc
#%{_libdir}/libefl_wl.so
%{_datadir}/eolian/include/efl-1/
#%{_includedir}/%{name}-wl-1/Efl_Wl.h

#----------------------------------------------------------------------------
#package -n %{libelocation}
#Summary:        Enlightenment geolocation libraries
#License:        BSD
#Group:          System/Libraries
#Requires:       %{name} = %{EVRD}
#
#description -n %{libelocation}
#Enlightenment geolocation libraries
#
#files -n %{libelocation}
#{_libdir}/libelocation.so.%{major}*

#----------------------------------------------------------------------------
#package -n %{develocation}
#Summary:	Elocation headers and development libraries
#License:	BSD
#Group:		Development/Other
#Requires:	%{libelocation} = %{EVRD}
#Requires:	%{develocation} = %{EVRD}
#
#description -n %{develocation}
#elocation headers and development libraries.
#
#files -n %{develocation}
#{_libdir}/libelocation.so
#{_libdir}/pkgconfig/elocation.pc
#{_includedir}/elocation-1/

#----------------------------------------------------------------------------
%package -n %{libemile}
Summary:        Enlightenment mile libraries
License:        BSD
Group:          System/Libraries
Requires:       %{name} = %{EVRD}

%description -n %{libemile}
Enlightenment geolocation libraries

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
elocation headers and development libraries.

%files -n %{devemile}
%{_libdir}/libemile.so
%{_libdir}/pkgconfig/emile.pc
%{_includedir}/emile-1/
%{_libdir}/cmake/Emile/

#----------------------------------------------------------------------------
%package -n %{libector}
Summary:        Enlightenment ector libraries
License:        BSD
Group:          System/Libraries
Requires:       %{libector} = %{EVRD}

%description -n %{libector}
Enlightenment geolocation libraries

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
#%{_datadir}/eolian/include/ector-1/

#----------------------------------------------------------------------------
%package -n 	%{libelput}
Summary:        Enlightenment mile libraries
License:        BSD
Group:          System/Libraries
Requires:       %{libelput} = %{EVRD}

%description -n %{libelput}
Enlightenment libraries

%files -n %{libelput}
%{_libdir}/libelput.so.%{major}*

#----------------------------------------------------------------------------
%package -n 	%{develput}
Summary:	elput headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libelput} = %{EVRD}
%description -n %{develput}
elput headers and development libraries.

%files -n %{develput}
%{_libdir}/libelput.so
%{_libdir}/pkgconfig/elput.pc
%{_includedir}/elput-1/Elput.h

#----------------------------------------------------------------------------

%package -n	elementary
Summary:        Basic widget set based on EFL for mobile touch-screen devices
License:        LGPLv2.1+
Group:          Graphical desktop/Enlightenment
Requires:	%{libelementary} = %{EVRD}

%description  -n elementary
A basic widget set that is easy to use based on EFL for mobile
touch-screen devices.

This package is part of the Enlightenment DR19 desktop shell.

%files -n elementary
%doc AUTHORS COPYING README
%{_bindir}/elementary_run
%{_bindir}/elementary_codegen
%{_bindir}/elementary_config
%{_bindir}/elementary_quicklaunch
%{_bindir}/elementary_perf
%{_bindir}/elm_prefs_cc
%{_libdir}/elementary/modules/access_output/v*
%{_libdir}/elementary/modules/prefs/v*
%{_datadir}/applications/elementary_config.desktop
%{_datadir}/applications/elementary_perf.desktop
%{_datadir}/elementary/config/*
%{_datadir}/elementary/edje_externals/*
%{_datadir}/elementary/images/*
%{_datadir}/elementary/themes/default.edj
%{_datadir}/elementary/objects/*
%{_datadir}/elementary/testdiff.diff
%{_datadir}/elementary/testfile-windows.txt
%{_datadir}/elementary/testfile-withblanks.txt
%{_datadir}/elementary/testfile.txt
%{_iconsdir}/Enlightenment-X/index.theme
%{_iconsdir}/Enlightenment-X/README
%{_iconsdir}/Enlightenment-X/*/*/*.png
%{_iconsdir}/hicolor/128x128/apps/elementary.png


#----------------------------------------------------------------------------

%package -n	%{libelementary}
Summary:        Libraries for the elementary package
Group:          System/Libraries
Requires:	%{libelementary} = %{EVRD}

%description -n %{libelementary}
Libraries for elementary

%files -n %{libelementary}
#%%doc AUTHORS COPYING README
%{_libdir}/libelementary.so.%{major}*
#{_libdir}/elementary/modules/clock_input_ctxpopup/v-%{shortver}/module.so
%{_libdir}/elementary/modules/web/none/*/module.so

#----------------------------------------------------------------------------

%package -n	%{develementary}
Summary:        Headers and development libraries from elementary
Group:          Development/Other
Requires:       %{libelementary} = %{EVRD}
Provides:       %{develementary} = %{EVRD}

%description -n %{develementary}
elementary development headers and libraries.

%files -n %{develementary}
#%%doc AUTHORS COPYING README
%{_bindir}/elementary_test
%{_libdir}/cmake/Elementary/
%{_libdir}/elementary/modules/test_entry/v*
%{_libdir}/elementary/modules/test_map/v*
%{_libdir}/pkgconfig/elementary*.*
%{_libdir}/libelementary.so
%{_datadir}/applications/elementary_test.desktop
%{_datadir}/eolian/include/elementary-1/*.eo*
%{_includedir}/elementary-1/*
%{_includedir}/elementary-cxx-1/*.hh

#----------------------------------------------------------------------------

%package -n efl_canvas_wl
Summary:	Enlightenment canvas library extra files
License:	BSD
Group:		Graphical desktop/Enlightenment

%description -n efl_canvas_wl
Enlightenment canvas library extra files.

Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

%files -n efl_canvas_wl
%{_bindir}/efl_canvas_wl_test*
%{_libdir}/libefl_canvas_wl.so.%{version}
%{_datadir}/eolian/include/efl-canvas-wl-1/efl_canvas_wl.eo
%{_datadir}/eolian/include/efl-canvas-wl-1/efl_canvas_wl_surface.eo

#----------------------------------------------------------------------------
%package -n 	%{libefl_canvas_wl}
Summary:        Enlightenment efl_canvas_wl libraries
License:        BSD
Group:          System/Libraries
Requires:       %{libefl_canvas_wl} = %{EVRD}
Requires:	      efl_canvas_wl = %{EVRD}

%description -n %{libefl_canvas_wl}
Enlightenment libraries

%files -n %{libefl_canvas_wl}
%{_libdir}/libefl_canvas_wl.so.%{major}*

#----------------------------------------------------------------------------

%package -n	%{devefl_canvas_wl}
Summary:        Headers and development libraries from efl_canvas_wl
Group:          Development/Other
Requires:       %{libefl_canvas_wl} = %{EVRD}
Requires:	      %{devefl} = %{EVRD}
Requires:       efl_canvas_wl = %{EVRD}
#Provides:       %{devefl_canvas_wl} = %{EVRD}
Provides:	      efl_canvas_wl-devel = %{EVRD}

%description -n %{devefl_canvas_wl}
elementary development headers and libraries.

%files -n %{devefl_canvas_wl}
%{_libdir}/libefl_canvas_wl.so
%{_libdir}/pkgconfig/efl-canvas-wl.pc
%{_includedir}/efl-canvas-wl-1/Efl_Canvas_Wl.h
%{_includedir}/efl-canvas-wl-1/efl_canvas_wl.eo.h
%{_includedir}/efl-canvas-wl-1/efl_canvas_wl_surface.eo.h

#----------------------------------------------------------------------------

%package -n exactness
Summary:	Enlightenment canvas library extra files
License:	BSD
Group:		Graphical desktop/Enlightenment

%description -n exactness
Enlightenment canvas library extra files.

Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

%files -n exactness
%{_bindir}/exactness*
%{_libdir}/libexactness_play.so.%{version}
%{_libdir}/libexactness_record.so.%{version}
%{_datadir}/exactness/player_entry.edj

#----------------------------------------------------------------------------
%package -n 	%{libexactness}
Summary:        Enlightenment exactness libraries
License:        BSD
Group:          System/Libraries
Requires:       %{libexactness} = %{EVRD}
Requires:	      %{name} = %{EVRD}
Requires:	      exactness = %{EVRD}

%description -n %{libexactness}
Enlightenment libraries

%files -n %{libexactness}
%{_libdir}/libexactness_play.so.%{major}*
%{_libdir}/libexactness_record.so.%{major}*

#----------------------------------------------------------------------------

%package -n	%{devexactness}
Summary:        Headers and development libraries from exactness
Group:          Development/Other
Requires:       %{libexactness} = %{EVRD}
Requires:	      %{devefl} = %{EVRD}
Requires:       exactness = %{EVRD}
#Provides:       %{devexactness} = %{EVRD}
Provides:	      exactness-devel = %{EVRD}

%description -n %{devexactness}
elementary development headers and libraries.

%files -n %{devexactness}
%{_libdir}/libexactness_play.so
%{_libdir}/libexactness_record.so


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
