%define gstapi 0.10
%define major 1

%define libecore %mklibname ecore %{major}
%define libecore_audio %mklibname ecore_audio %{major}
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

%define libephysics %mklibname ephysics %{major}
%define devephysics %mklibname ephysics -d

%define libethumb %mklibname ethumb %{major}
%define libethumb_client %mklibname ethumb_client %{major}
%define devethumb %mklibname ethumb -d

%define libevas %mklibname evas %{major}
%define devevas %mklibname evas -d

%define devname %mklibname %{name} -d

Summary:	Enlightenment Foundation Libraries
Name:		efl
Version:	1.8.3
Release:	1
Epoch:		3
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/rel/libs/efl/%{name}-%{version}.tar.bz2
BuildRequires:	doxygen
BuildRequires:	gstreamer%{gstapi}-tools
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	jpeg-devel
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
BuildRequires:	pkgconfig(libsystemd-daemon)
BuildRequires:	pkgconfig(libsystemd-journal)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(mount)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(sndfile)
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
%{_datadir}/ecore/
%{_datadir}/ecore_imf/
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

%package -n %{devecore}
Summary:	Ecore headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{libecore} = %{EVRD}
Requires:	%{libecore_audio} = %{EVRD}
Requires:	%{libecore_con} = %{EVRD}
Requires:	%{libecore_evas} = %{EVRD}
Requires:	%{libecore_file} = %{EVRD}
Requires:	%{libecore_imf} = %{EVRD}
Requires:	%{libecore_imf_evas} = %{EVRD}
Requires:	%{libecore_input} = %{EVRD}
Requires:	%{libecore_input_evas} = %{EVRD}
Requires:	%{libecore_ipc} = %{EVRD}
Requires:	%{libecore_sdl} = %{EVRD}
Requires:	%{libecore_x} = %{EVRD}
Provides:	ecore-devel = %{EVRD}

%description -n %{devecore}
Ecore headers and development libraries.

%files -n %{devecore}
%{_libdir}/cmake/Ecore/
%{_libdir}/pkgconfig/ecore.pc
%{_libdir}/pkgconfig/ecore-audio.pc
%{_libdir}/pkgconfig/ecore-con.pc
%{_libdir}/pkgconfig/ecore-evas.pc
%{_libdir}/pkgconfig/ecore-file.pc
%{_libdir}/pkgconfig/ecore-imf.pc
%{_libdir}/pkgconfig/ecore-imf-evas.pc
%{_libdir}/pkgconfig/ecore-input.pc
%{_libdir}/pkgconfig/ecore-input-evas.pc
%{_libdir}/pkgconfig/ecore-ipc.pc
%{_libdir}/pkgconfig/ecore-sdl.pc
%{_libdir}/pkgconfig/ecore-x.pc
%{_libdir}/libecore.so
%{_libdir}/libecore_audio.so
%{_libdir}/libecore_con.so
%{_libdir}/libecore_evas.so
%{_libdir}/libecore_file.so
%{_libdir}/libecore_imf.so
%{_libdir}/libecore_imf_evas.so
%{_libdir}/libecore_input.so
%{_libdir}/libecore_input_evas.so
%{_libdir}/libecore_ipc.so
%{_libdir}/libecore_sdl.so
%{_libdir}/libecore_x.so
%{_includedir}/ecore-1/
%{_includedir}/ecore-audio-1/
%{_includedir}/ecore-con-1/
%{_includedir}/ecore-evas-1/
%{_includedir}/ecore-file-1/
%{_includedir}/ecore-imf-1/
%{_includedir}/ecore-imf-evas-1/
%{_includedir}/ecore-input-1/
%{_includedir}/ecore-input-evas-1/
%{_includedir}/ecore-ipc-1/
%{_includedir}/ecore-sdl-1/
%{_includedir}/ecore-x-1/

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
Provides:	edje-devel = %{EVRD}

%description -n %{devedje}
Edje headers and development libraries.

%files -n %{devedje}
%{_libdir}/cmake/Edje/
%{_libdir}/pkgconfig/edje.pc
%{_libdir}/libedje.so
%{_includedir}/edje-1/

#----------------------------------------------------------------------------

%package -n eet
Summary:	Enlightenment simple compression utility
License:	BSD
Group:		Graphical desktop/Enlightenment

%description -n eet
Enlightenment simple compression utility.

%files -n eet
%{_bindir}/eet

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
Provides:	eet-devel = %{EVRD}

%description -n %{deveet}
Eet headers and development libraries.

%files -n %{deveet}
%{_libdir}/cmake/Eet/
%{_libdir}/pkgconfig/eet.pc
%{_libdir}/libeet.so
%{_includedir}/eet-1/

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
%{_libexecdir}/efreet/*/efreet_desktop_cache_create
%{_libexecdir}/efreet/*/efreet_icon_cache_create

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
Provides:	eina-devel = %{EVRD}

%description -n %{deveina}
Eina headers and development libraries.

%files -n %{deveina}
%{_libdir}/cmake/Eina/
%{_libdir}/pkgconfig/eina.pc
%{_libdir}/libeina.so
%{_includedir}/eina-1/

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
Provides:	eio-devel = %{EVRD}

%description -n %{deveio}
Eio headers and development libraries.

%files -n %{deveio}
%{_libdir}/pkgconfig/eio.pc
%{_libdir}/libeio.so
%{_includedir}/eio-1/

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
Provides:	eldbus-devel = %{EVRD}

%description -n %{develdbus}
Eldbus headers and development libraries.

%files -n %{develdbus}
%{_libdir}/cmake/Eldbus/
%{_libdir}/pkgconfig/eldbus.pc
%{_libdir}/libeldbus.so
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
Provides:	emotion-devel = %{EVRD}

%description -n %{devemotion}
Emotion headers and development libraries.

%files -n %{devemotion}
%{_libdir}/pkgconfig/emotion.pc
%{_libdir}/libemotion.so
%{_includedir}/emotion-1/

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
Provides:	eo-devel = %{EVRD}

%description -n %{deveo}
Eo headers and development libraries.

%files -n %{deveo}
%{_libdir}/cmake/Eo/
%{_libdir}/pkgconfig/eo.pc
%{_libdir}/libeo.so
%{_includedir}/eo-1/
%{_datadir}/gdb/auto-load/%{_libdir}/libeo.so.*-gdb.py
%{_datadir}/eo/gdb/eo_gdb.py

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
%{_libdir}/evas/modules/loaders/*/*/*.so
%{_libdir}/evas/modules/savers/*/*/*.so
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
Provides:	evas-devel = %{EVRD}

%description -n %{devevas}
Evas headers and development libraries.

%files -n %{devevas}
%{_libdir}/cmake/Evas/
%{_libdir}/pkgconfig/evas.pc
%{_libdir}/pkgconfig/evas-opengl-sdl.pc
%{_libdir}/pkgconfig/evas-opengl-x11.pc
%{_libdir}/pkgconfig/evas-software-buffer.pc
%{_libdir}/pkgconfig/evas-software-x11.pc
%{_libdir}/libevas.so
%{_includedir}/evas-1/

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	EFL headers and development libraries
License:	BSD
Group:		Development/Other
Requires:	%{devecore} = %{EVRD}
Requires:	%{devedje} = %{EVRD}
Requires:	%{deveet} = %{EVRD}
Requires:	%{deveeze} = %{EVRD}
Requires:	%{devefreet} = %{EVRD}
Requires:	%{deveina} = %{EVRD}
Requires:	%{deveio} = %{EVRD}
Requires:	%{develdbus} = %{EVRD}
Requires:	%{devembryo} = %{EVRD}
Requires:	%{devemotion} = %{EVRD}
Requires:	%{deveo} = %{EVRD}
Requires:	%{devephysics} = %{EVRD}
Requires:	%{devethumb} = %{EVRD}
Requires:	%{devevas} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
EFL headers and development libraries.

%files -n %{devname}
%{_includedir}/efl-1/

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--enable-fontconfig \
	--enable-gstreamer \
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
	--enable-sdl \
	--enable-systemd \
	--enable-v4l2 \
	--enable-xine \
	--with-eject \
	--with-mount \
	--with-umount \
	--disable-static \

%make

%install
%makeinstall_std

%find_lang %{name}
