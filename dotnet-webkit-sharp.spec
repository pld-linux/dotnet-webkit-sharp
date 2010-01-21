%include	/usr/lib/rpm/macros.mono
Summary:	WebKit# - A Mono WebKit binding
Summary(pl.UTF-8):	WebKit# - wiązanie WebKit dla Mono
Name:		dotnet-webkit-sharp
Version:	0.3
Release:	1
License:	X11/MIT
Group:		Libraries
Source0:	http://ftp.novell.com/pub/mono/sources/webkit-sharp/webkit-sharp-%{version}.tar.bz2
# Source0-md5:	21482f9d5eafb0ef4acc6e790482f934
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 1.9.3
BuildRequires:	gtk-webkit-devel >= 1.1.15
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
WebKit to silnik przeglądarki internetowej, wywodzący się z projektów
KHTML i KJS dla platformy KDE, używany głównie w przeglądarce Safari
firmy Apple. Stworzony został aby móc osadzać go w innych aplikacjach,
takich jak czytniki poczty czy przeglądarki stron internetowych.

Ten pakiet dostarcza dowiązań Mono do bibliotek WebKit.

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
%setup -q -n webkit-sharp-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docsdir=%{_libdir}/monodoc/sources \
	pkgconfigdir=%{_pkgconfigdir}

install samples/*.cs $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
%{_examplesdir}/%{name}-%{version}
