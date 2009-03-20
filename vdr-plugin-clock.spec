
%define plugin	clock
%define name	vdr-plugin-%plugin
%define version	1.0.0
%define rel	3

Summary:	VDR plugin: A Simple Clock
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://vdr.humpen.at/
Source:		http://vdr.humpen.at/uploads/media/vdr-%plugin-%version.tgz
Patch0:		clock-1.0.0-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
My Humax Receiver has a Clock Function that I enjoy very much.
So I decided to write a Plugin for VDR which allows me to see
a small clock in the Top right corner.

The Idea is to set a unused key from your remote control
(for example the key User1) to show the clock.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


