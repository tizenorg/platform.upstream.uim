Name:           uim
Version: 	0.1
Release:	1
License:	GPLv2+
Summary:	User Mode Init manager for bluetooth device in pr3	
Group:		Communications/Bluetooth
Source:		%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(bluez)

%description
User Mode Init manager for tiwl1283

%prep
%setup -q

%build
gcc -o uim uim.c

%install
mkdir -p %{buildroot}/bin/
cp -f uim %{buildroot}/bin/

%files
%attr(0755,-,-) /bin/uim
