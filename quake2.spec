%define ver 6_00
Name:           quake2
Version:        6.00
Release:        3%{?dist}
Summary:        Quake II (Yamagi version)
License:        GPLv2 
URL:            http://www.yamagi.org/quake2 
Source0:        https://github.com/yquake2/yquake2/archive/QUAKE2_%{ver}.tar.gz
Source1:        %{name}.desktop
Patch0:         allow-custom-cflags.patch
Patch1:         remove-rpaths.patch
BuildRequires:  mesa-libGL-devel,SDL2-devel,libogg-devel,libvorbis-devel
BuildRequires:  openal-soft-devel,zlib-devel,desktop-file-utils

%description
This package contains the enhanced GPL YamagiQuake2 version of the Quake 2 
engine.
To run the game you will need the original data files from demo or 
full versions.

Full version setup:
Copy the baseq2 folder contents from the CD-ROM/Steam to ~/.yq2/baseq2/ 
(or to use the data files system-wide copy the data files to 
%{_libdir}/games/%{name}/baseq2/)
Enjoy the full version.

Demo version setup:
Get the demo from http://deponie.yamagi.org/quake2/idstuff/q2-314-demo-x86.exe 
and extract it. 
It's just an ordinary, self-extract ZIP file. 
An archiver or even the unzip command can be used. 
copy the extracted folder contents /Install/Data/baseq2/* to ~/.yq2/baseq2/ 
(or to use the data files system-wide copy the data files to 
%{_libdir}/games/%{name}/baseq2/)
Enjoy the demo version.

Not patched full version setup:
If your full version of quake 2 isn't patched you need to do some more steps
Please note that the patch is required for all full versions of the game, 
even the newer ones like Steam. Without it Yamagi Quake II will not work!

Download the patch: 
http://deponie.yamagi.org/quake2/idstuff/q2-3.20-x86-full-ctf.exe
Extract the patch into an empty directory. The patch is just an ordinary 
self-extracting ZIP file. On Windows it can be extracted by double clicking 
on it, on other systems an archiver or even the unzip command can be used.

Now it's time to remove the following files from the extracted patch. 
They're the original executables, documentation and so on. 
They aren't needed anymore:

3.20_Changes.txt
quake2.exe
ref_gl.dll
ref_soft.dll
baseq2/gamex86.dll
baseq2/maps.lst
ctf/ctf2.ico
ctf/gamex86.dll
ctf/readme.txt
ctf/server.cfg
xatrix/gamex86.dll
rogue/gamex86.dll

Copy the pak0.pak file and the video/ sub-directory from your Quake II 
distribution (CD, Steam download, etc) into the baseq2/ sub-directory 
of the extracted patch.
%prep
%autosetup -n yquake2-QUAKE2_%{ver}


%build
CFLAGS="%{optflags}" make %{?_smp_mflags} \
    WITH_SYSTEMWIDE=yes \
    WITH_SYSTEMDIR='%{_libdir}/games/%{name}'

%make_build

%install

%{__install} -D -p -m 755 release/quake2 %{buildroot}%{_bindir}/quake2
%{__install} -D -p -m 755 release/q2ded %{buildroot}%{_bindir}/q2ded
%{__install} -D -p -m 755 release/baseq2/game.so \
    %{buildroot}%{_libdir}/games/%{name}/baseq2/game.so
%{__install} -D -p -m 644 stuff/yq2.cfg \
    %{buildroot}%{_libdir}/games/%{name}/baseq2/yq2.cfg
%{__install} -D -p -m 644 stuff/icon/Quake2.svg \
    %{buildroot}%{_datadir}/pixmaps/quake2.svg
%{__install} -D -p -m 755 stuff/cdripper.sh \
    %{buildroot}%{_defaultdocdir}/%{name}/examples/cdripper.sh
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%license LICENSE
%doc CHANGELOG CONTRIBUTE README.md
%{_bindir}/*
%{_libdir}/games/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/* 
%{_defaultdocdir}/%{name}/*



%changelog
* Sat Feb 04 2017 Frederico Lima <fredlima@fedoraproject.org> - 6.00-3
- fixed missing Icon

* Sat Feb 04 2017 Frederico Lima <fredlima@fedoraproject.org> - 6.00-2
- Added an patch to remove the rpaths from the makefile

* Fri Feb 03 2017 Frederico Lima <fredlima@fedoraproject.org> - 6.00-1
- Changed the package version from 5.34 to 6.00

* Fri Jul 29 2016 Frederico Lima <fredlima@fedoraproject.org> - 5.34-5
- Updated file section to remove a few files left behing

* Thu Jul 28 2016 Frederico Lima <fredlima@fedoraproject.org> - 5.34-4
- Removed unnecessary sections
- Use of install macro instead of mkdir and cp

* Thu Jul 28 2016 Frederico Lima <fredlima@fedoraproject.org> - 5.34-3
- Fixed issues taken from rpmlint

* Thu Jul 28 2016 Frederico Lima <fredlima@fedoraproject.org> - 5.34-2
- Changed the package version from 2.5.34 to 5.34

* Sun Jul 24 2016 Frederico Lima <fredlima@fedoraproject.org> - 5.34-1
- Initial Fedora RPM release
- Added allow-custom-cflags.patch from rpm@fthiessen.de to allow custom cflags
- Compile with optflags
