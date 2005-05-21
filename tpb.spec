Summary:	Utility to enable the IBM ThinkPad(tm) special keys
Summary(pl):	Narz�dzie uaktywniaj�ce klawisze specjalne w notebookach IBM ThinkPad(tm)
Name:		tpb
Version:	0.6.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://savannah.nongnu.org/download/tpb/%{name}-%{version}.tar.gz
# Source0-md5:	fc11a0af992178e4013fd9c041dbaa7e
Source1:	%{name}-pl.po
Patch0:		%{name}-lang_pl.patch
URL:		http://savannah.gnu.org/projects/tpb/
BuildRequires:	xosd-devel >= 2.0.0
Requires:	xosd >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program enables the IBM Thinkpad(tm) special keys. It is possible
to bind a program to the ThinkPad button. It has a on-screen display
(OSD) to show volume, mute and brightness of the LCD.

%description -l pl
Program ten uaktywnia klawisze specjalne w notebookach IBM
ThinkPad(tm). Umo�liwia r�wnie� programowanie przycisk�w specjalnych,
wspiera r�wnie� OSD (d�wi�k, kontrast LCD).

%prep
%setup -q
cp %{SOURCE1} po/pl.po

%patch0 -p1

%build
%configure2_13

%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/callback_example.sh ChangeLog CREDITS README TODO doc/tpbrc
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/tpbrc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
