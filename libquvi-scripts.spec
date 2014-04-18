Summary:	Embedded lua scripts that libquvi uses for parsing the media details
Name:		libquvi-scripts
Version:	0.9.20131130
Release:	1
License:	LGPL v2.1+
Group:		Applications
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
# Source0-md5:	46ddfd887260a515199c2e1ba8c46d8a
URL:		http://quvi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains embedded lua scripts that libquvi uses for
parsing the media details.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--host=%{_host}		\
	--build=%{_build}	\
	--disable-silent-rules	\
	--with-nlfy		\
	--with-nsfw
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_npkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/%{name}
%{_mandir}/man7/*quvi*.7*
%{_npkgconfigdir}/libquvi-scripts-0.9.pc

