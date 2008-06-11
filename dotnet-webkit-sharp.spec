%define	snap	105457

%include	/usr/lib/rpm/macros.mono
Summary:	WebKit# - A Mono WebKit binding
Summary(pl.UTF-8):	WebKit# - wiązanie WebKit dla Mozilli
Name:		dotnet-webkit-sharp
Version:	0.2
Release:	0.%{snap}.1
License:	X11/MIT
Group:		Libraries
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	0e529b41b394e4188ae5b8b19b0914e4
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 1.9.3
BuildRequires:	gtk-webkit-devel
BuildRequires:	mono-csharp >= 1.1.0
BuildRequires:	monodoc >= 1.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser. It is made to be
embedded in other applications, such as mail readers, or web browsers.

This package provides Mono bindings for WebKit libraries.

%description -l pl.UTF-8

%package devel
Summary:	WebKit# development files
Summary(pl.UTF-8):	Pliki programistyczne WebKit#
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
WebKit# development files.

%description devel -l pl.UTF-8
Pliki programistyczne WebKit#.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	monodocdir=%{_libdir}/monodoc/sources \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{_prefix}/lib/mono/gac/webkit-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/webkit-sharp
%{_pkgconfigdir}/*
%{_libdir}/monodoc/sources/*
