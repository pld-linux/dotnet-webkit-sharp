Summary:	WebKit# - A Mono WebKit binding
Summary(pl.UTF-8):	WebKit# - wiązanie WebKit dla Mono
Name:		dotnet-webkit-sharp
Version:	0.3
Release:	5
License:	MIT
Group:		Libraries
Source0:	http://download.mono-project.com/sources/webkit-sharp/webkit-sharp-%{version}.tar.bz2
# Source0-md5:	21482f9d5eafb0ef4acc6e790482f934
Patch0:		%{name}-pc.patch
URL:		http://www.mono-project.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 1.9.3
BuildRequires:	gtk-webkit-devel >= 1.1.15
BuildRequires:	mono-csharp >= 1.1.0
BuildRequires:	monodoc >= 2.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Requires:	dotnet-gtk-sharp2 >= 1.9.3
Requires:	gtk-webkit >= 1.1.15
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

Ten pakiet dostarcza wiązania Mono do bibliotek WebKit.

%package devel
Summary:	WebKit# development files
Summary(pl.UTF-8):	Pliki programistyczne WebKit#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel >= 1.9.3
Requires:	monodoc >= 2.6

%description devel
WebKit# development files.

%description devel -l pl.UTF-8
Pliki programistyczne WebKit#.

%prep
%setup -q -n webkit-sharp-%{version}
%patch -P0 -p1

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
	DESTDIR=$RPM_BUILD_ROOT

install samples/*.cs $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%{_prefix}/lib/mono/gac/webkit-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/webkit-sharp
%{_pkgconfigdir}/webkit-sharp-1.0.pc
%{_prefix}/lib/monodoc/sources/webkit-sharp-docs.*
%{_examplesdir}/%{name}-%{version}
