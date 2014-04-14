Summary:	Graphical directory tree analyzer
Name:		baobab
Version:	3.12.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/baobab/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	1d265bf555143f7aa0a7d961fd8126c2
URL:		http://live.gnome.org/GnomeUtils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	intltool
BuildRequires:	pkg-config
BuildRequires:	vala-vapigen >= 0.24.0
BuildRequires:	yelp-tools
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical directory tree analyzer for GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/baobab
%{_datadir}/dbus-1/services/org.gnome.baobab.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_desktopdir}/org.gnome.baobab.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/baobab.1*

