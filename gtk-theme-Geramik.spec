
%define		_theme		Geramik

Summary:	GTK theme similar to the Keramik KDE style
Summary(pl):	Motyw dla GTK podobny do stylu Keramik dla KDE
Name:		gtk-theme-%{_theme}
Version:	0.24
Release:	1
License:	GPL v2
Group:		Themes/Gtk
Source0:	http://www.kde-look.org/content/files/3952-%{_theme}-%{version}.tar.gz
BuildRequires:	gtk+
BuildRequires:	gtk+2
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK theme intended to make GTK applications have a similar look to the
Keramik KDE style.

%description -l pl
Motyw dla GTK, maj±cy na celu nadanie aplikacjom GTK wygl±du podobnego
do stylu Keramik dla KDE.

%package common
Summary:	Geramik GTK theme - common files
Summary(pl):	Motyw dla GTK - Geramik - pliki wspólne
Group:		Themes/Gtk

%description common
GTK theme intended to make GTK applications have a similar look to the
Keramik KDE style.

This package contains common files for gtk+ and gtk+2.

%description common -l pl
Motyw dla GTK, maj±cy na celu nadanie aplikacjom GTK wygl±du podobnego
do stylu Keramik dla KDE.

Ten pakiet zawiera pliki wspólne dla gtk+ i gtk+2.

%package gtk1
Summary:	GTK theme similar to the Keramik KDE style
Summary(pl):	Motyw dla GTK podobny do stylu Keramik dla KDE
Group:		Themes/Gtk
Requires:	%{name}-common
Requires:	gtk+

%description gtk1
GTK theme intended to make GTK applications have a similar look to the
Keramik KDE style.

This package contains theme for applications based on gtk+.

%description gtk1 -l pl
Motyw dla GTK, maj±cy na celu nadanie aplikacjom GTK wygl±du podobnego
do stylu Keramik dla KDE.

Ten pakiet zawiera motyw dla aplikacji opartych na gtk+.

%package gtk2
Summary:	GTK theme similar to the Keramik KDE style
Summary(pl):	Motyw dla GTK podobny do stylu Keramik dla KDE
Group:		Themes/Gtk
Requires:	%{name}-common
Requires:	gtk+2

%description gtk2
GTK theme intended to make GTK applications have a similar look to the
Keramik KDE style.

This package contains theme for applications based on gtk+2.

%description gtk2 -l pl
Motyw dla GTK, maj±cy na celu nadanie aplikacjom GTK wygl±du podobnego
do stylu Keramik dla KDE.

Ten pakiet zawiera motyw dla aplikacji opartych na gtk+2.

%prep
%setup -q -n %{_theme}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%dir %{_datadir}/themes/%{_theme}
%{_datadir}/themes/Geramik/README.html

%files gtk1
%defattr(644,root,root,755)
%{_libdir}/gtk/themes/engines/*.la
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*.so
%{_datadir}/themes/%{_theme}/gtk

%files gtk2
%defattr(644,root,root,755)
%{_libdir}/gtk-2.0/2.2.0/engines/*.la
%attr(755,root,root) %{_libdir}/gtk-2.0/2.2.0/engines/*.so
%{_datadir}/themes/%{_theme}/gtk-2.0
