%define version 0.0.14.1
%define release %mkrel 4

%define libggz_version %{version}
%define ggz_client_libs_version %{version}

Name:		ggz-utils
Summary:	GGZ Utilities
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Other
URL:		https://www.ggzgamingzone.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	http://ftp.ggzgamingzone.org/pub/ggz/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	libggz-devel = %{libggz_version}
BuildRequires:	ggz-client-libs-devel = %{ggz_client_libs_version}
Requires:	libggz = %{libggz_version}
Requires:	ggz-client-libs = %{ggz_client_libs_version}

%description
This package contains some assorted utilities which don't fit into
another GGZ Gaming Zone packages:

- Cmd-Client:
  Utily to broadcast messages across all rooms at a GGZ server.
- Metaserv:
  The first prototype of a GGZ meta server. It is completely XML-based
  but understands URI queries as well.
- ggzcommgen:
  A GGZ Communication Library source file generator.
- TelGGZ:
  A Telnet wrapper for GGZ. Using telggz you can chat from
  everywhere in the world, provided you get a telnet terminal.

%prep
%setup -q

%build
%configure2_5x --bindir=%{_gamesbindir} --with-libggz-libraries=%{_libdir} --with-ggzcore-libraries=%{_libdir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_gamesbindir}/*
%{_mandir}/man1/*
%{_datadir}/ggzmetaserv


