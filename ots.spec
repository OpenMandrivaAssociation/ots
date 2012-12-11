%define api		1
%define major	0
%define libname		%mklibname %{name} %{api} %{major}
%define develname 	%mklibname ots -d

Name:		ots
Summary:	A text summarizer
Version:	0.5.0
Release:	8
License:	GPLv2+
Group:		System/Libraries
URL:		http://libots.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
Patch0:		ots-0.5.0-fix-underlinking.patch
Patch1:		ots-0.5.0-fix-installation.patch

BuildRequires:	popt-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
The open text summarizer is an open source tool for summarizing texts.
The program reads a text and decides which sentences are important and
which are not.
The program can either print the summarized text in text format or in
HTML form where the important sentences are highlighted in red.
 
The program is multi lingual and work with UTF-8 code;  At the moment
only English Hebrew are supported.
 
The ots command line tool is an example and a debug tool for the libary.
You can bind to the library from your program.

%package -n %{libname}
Summary:	Libraries for ots
Group:		System/Libraries

%description -n %{libname}
This package provides the libraries for using ots.

%package -n %{develname}
Summary:	Libraries and include files for developing with libots
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package provides the necessary development libraries and include
files to allow you to develop with libots.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
touch gtk-doc.make
autoreconf -fi
%configure2_5x \
	--disable-gtk-doc \
	--disable-static

%make -j1

%install
%makeinstall_std

# clean out unused files
rm -rf %{buildroot}%{_datadir}/doc/libots/html/*

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/%{name}
%dir %{_datadir}/ots
%{_datadir}/ots/*

%files -n %{libname}
%{_libdir}/libots-%{api}.so.%{major}*

%files -n %{develname}
%{_libdir}/libots-%{api}.so
%dir %{_includedir}/libots-%{api}
%dir %{_includedir}/libots-%{api}/ots
%{_includedir}/libots-%{api}/ots/*.h
%{_libdir}/pkgconfig/libots-%{api}.pc



%changelog
* Sun Mar 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.5.0-8
+ Revision: 786630
- rebuild
- cleaned up spec

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Mon Jun 01 2009 Funda Wang <fwang@mandriva.org> 0.5.0-6mdv2010.0
+ Revision: 381750
- fix installation

* Sat Jul 05 2008 Funda Wang <fwang@mandriva.org> 0.5.0-6mdv2009.0
+ Revision: 231928
- new license policy & devel package name policy

* Sat Jul 05 2008 Funda Wang <fwang@mandriva.org> 0.5.0-5mdv2009.0
+ Revision: 231927
- renew tarball with official tarball
- fix underlinking
- fix building .so files

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 04 2007 Funda Wang <fwang@mandriva.org> 0.5.0-5mdv2008.0
+ Revision: 22226
- build shared libraries.
- another finally fix for requires, cause the orginal libname is wrong.
- fix provides on 64 bit

* Fri May 04 2007 Funda Wang <fwang@mandriva.org> 0.5.0-4mdv2008.0
+ Revision: 22198
- finally fix requires

* Fri May 04 2007 Funda Wang <fwang@mandriva.org> 0.5.0-3mdv2008.0
+ Revision: 22197
- bump release
- Corrected requires.

* Thu May 03 2007 Funda Wang <fwang@mandriva.org> 0.5.0-2mdv2008.0
+ Revision: 21764
- no more .so files.
- use autogen
- Renew tarball with CVS latest.
- kill doc dir now due to missing gtk-doc.make in tarball
- New version 0.5.0
- Import ots




* Mon Jan 17 2005 Marcel Pol <mpol@mandrake.org> 0.4.2-2mdk
- rebuild

* Wed Dec 10 2003 Marcel Pol <mpol@mandrake.org> 0.4.2-1mdk
- 0.4.2

* Sat Aug 30 2003 Marcel Pol <mpol@gmx.net> 0.4.1-3mdk
- buildrequires again

* Fri Aug 29 2003 Marcel Pol <mpol@gmx.net> 0.4.1-2mdk
- buildrequires

* Thu Aug 14 2003 Marcel Pol <mpol@gmx.net> 0.4.1-1mdk
- initial mandrake contrib
- libpolicy and small changes

* Thu Jun 05 2003 Rui Miguel Silva Seabra <rms@1407.org>
- fix spec
- disable gtk-doc (it's not building in RH 9,
  maybe it's broken for some reason)

* Fri May 02 2003 Rui Miguel Silva Seabra <rms@1407.org>
- define a longer description from the README file
- explicitly set file permissions

* Wed Apr 30 2003 Dom Lachowicz <cinamod@hotmail.com>
- created this thing
