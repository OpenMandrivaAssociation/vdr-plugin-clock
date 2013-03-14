
%define plugin	clock
%define name	vdr-plugin-%plugin
%define version	1.0.0
%define rel	5

Summary:	VDR plugin: A Simple Clock
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://vdr.humpen.at/
Source:		http://vdr.humpen.at/uploads/media/vdr-%plugin-%version.tgz
Patch0:		clock-1.0.0-i18n-1.6.patch
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
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 1.0.0-4mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 1.0.0-3mdv2009.1
+ Revision: 359301
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 1.0.0-2mdv2009.0
+ Revision: 197913
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 1.0.0-1mdv2009.0
+ Revision: 197645
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- drop previous patches, fixed upstream

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.6-12mdv2008.1
+ Revision: 145051
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6-11mdv2008.1
+ Revision: 103077
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6-10mdv2008.0
+ Revision: 49983
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6-9mdv2008.0
+ Revision: 42070
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6-8mdv2008.0
+ Revision: 22732
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-7mdv2007.0
+ Revision: 90905
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-6mdv2007.1
+ Revision: 73977
- rebuild for new vdr
- Import vdr-plugin-clock

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-4mdv2007.0
- stricter abi requires
- patch2: do not create empty ../../man during build

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-2mdv2007.0
- rebuild for new vdr

* Wed Jun 21 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-1mdv2007.0
- initial Mandriva release

