Summary:	Graphical directory tree analyzer
Name:		baobab
Version:	3.6.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/baobab/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	ed27564a6ea6561a9d820cfb575e3d39
URL:		http://live.gnome.org/GnomeUtils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	pkg-config
BuildRequires:	vala-vapigen
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
%{__aclocal} -I m4 -I libgd
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
%{_datadir}/glib-2.0/schemas/*.xml
%{_desktopdir}/baobab.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/baobab.1*

