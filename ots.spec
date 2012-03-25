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

