
%define		theme		Geramik

Summary:	GTK+ theme similar to the Keramik KDE style
Summary(pl.UTF-8):	Motyw dla GTK+ podobny do stylu Keramik dla KDE
Name:		gtk-theme-%{theme}
Version:	0.24
Release:	2
License:	GPL v2
Group:		Themes/GTK+
Source0:	http://www.kde-look.org/content/files/3952-%{theme}-%{version}.tar.gz
# Source0-md5:	f632116374c07a6f1e566442f6705533
Patch0:		%{name}-comment.patch
BuildRequires:	gtk+-devel >= 1:1.2.9
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	imlib-devel >= 1.8.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ theme intended to make GTK+ applications have a similar look to
the Keramik KDE style.

%description -l pl.UTF-8
Motyw dla GTK+, mający na celu nadanie aplikacjom GTK+ wyglądu
podobnego do stylu Keramik dla KDE.

%package common
Summary:	Geramik GTK+ theme - common files
Summary(pl.UTF-8):	Motyw dla GTK+ - Geramik - pliki wspólne
Group:		Themes/GTK+

%description common
GTK+ theme intended to make GTK+ applications have a similar look to the
Keramik KDE style.

This package contains common files for GTK+ and GTK+2.

%description common -l pl.UTF-8
Motyw dla GTK+, mający na celu nadanie aplikacjom GTK+ wyglądu podobnego
do stylu Keramik dla KDE.

Ten pakiet zawiera pliki wspólne dla GTK+ i GTK+2.

%package gtk1
Summary:	GTK+ theme similar to the Keramik KDE style
Summary(pl.UTF-8):	Motyw dla GTK+ podobny do stylu Keramik dla KDE
Group:		Themes/GTK+
Requires:	%{name}-common = %{version}-%{release}
Requires:	gtk+ >= 1:1.2.9
Requires:	imlib >= 1.8.0

%description gtk1
GTK+ theme intended to make GTK+ applications have a similar look to the
Keramik KDE style.

This package contains theme for applications based on GTK+.

%description gtk1 -l pl.UTF-8
Motyw dla GTK+, mający na celu nadanie aplikacjom GTK+ wyglądu podobnego
do stylu Keramik dla KDE.

Ten pakiet zawiera motyw dla aplikacji opartych na GTK+.

%package gtk2
Summary:	GTK+ theme similar to the Keramik KDE style
Summary(pl.UTF-8):	Motyw dla GTK+ podobny do stylu Keramik dla KDE
Group:		Themes/GTK+
Requires:	%{name}-common = %{version}-%{release}

%description gtk2
GTK+ theme intended to make GTK+ applications have a similar look to the
Keramik KDE style.

This package contains theme for applications based on GTK+2.

%description gtk2 -l pl.UTF-8
Motyw dla GTK+, mający na celu nadanie aplikacjom GTK+ wyglądu podobnego
do stylu Keramik dla KDE.

Ten pakiet zawiera motyw dla aplikacji opartych na GTK+2.

%prep
%setup -q -n %{theme}-%{version}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines/*.la
rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%dir %{_datadir}/themes/%{theme}
%{_datadir}/themes/Geramik/README.html

%files gtk1
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*.so
%{_datadir}/themes/%{theme}/gtk

%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_datadir}/themes/%{theme}/gtk-2.0
