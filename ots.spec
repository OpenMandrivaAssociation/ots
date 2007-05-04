
%define api_version     1
%define lib_major       0
%define lib_name        %mklibname %{name}- %{api_version} %{lib_major}

Name:		ots
Summary:	A text summarizer
Version:	0.5.0
Release:	%mkrel 5
License:	GPL
Group:		System/Libraries
URL:		http://libots.sourceforge.net/
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	pkgconfig >= 0.8
BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	popt-devel
#BuildRequires:	gtk-doc

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

%package -n %{lib_name}
Summary:	Libraries for ots
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n %{lib_name}
This package provides the libraries for using ots.


%package -n %{lib_name}-devel
Summary:	Libraries and include files for developing with libots
Group:		Development/C
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-devel
# not sure if this provides is correct
Provides:	libots-1-devel

%description -n %{lib_name}-devel
This package provides the necessary development libraries and include
files to allow you to develop with libots.


%prep
%setup -q -n ots-%{version}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x --disable-gtk-doc --disable-static
%make -j1

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

# clean out unused files
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libots/html/*


%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0755,root,root)%{_bindir}/%{name}
%defattr(0644, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
#%{_mandir}/*/*
%dir %{_datadir}/ots
%{_datadir}/ots/*

%files -n %{lib_name}
%defattr(0644, root, root, 0755)
%{_libdir}/*ots-1.so.*

%files -n %{lib_name}-devel
%defattr(0644, root, root, 0755)
%{_libdir}/*ots-1.so
%{_libdir}/*.*a
%dir %{_includedir}/libots-1
%dir %{_includedir}/libots-1/ots
%{_includedir}/libots-1/ots/*.h
%{_libdir}/pkgconfig/libots-1.pc
