{*
* 2007-2015 PrestaShop
*
* NOTICE OF LICENSE
*
* This source file is subject to the Academic Free License (AFL 3.0)
* that is bundled with this package in the file LICENSE.txt.
* It is also available through the world-wide-web at this URL:
* http://opensource.org/licenses/afl-3.0.php
* If you did not receive a copy of the license and are unable to
* obtain it through the world-wide-web, please send an email
* to license@prestashop.com so we can send you a copy immediately.
*
* DISCLAIMER
*
* Do not edit or add to this file if you wish to upgrade PrestaShop to newer
* versions in the future. If you wish to customize PrestaShop for your
* needs please refer to http://www.prestashop.com for more information.
*
*  @author PrestaShop SA <contact@prestashop.com>
*  @copyright  2007-2015 PrestaShop SA
*  @license    http://opensource.org/licenses/afl-3.0.php  Academic Free License (AFL 3.0)
*  International Registered Trademark & Property of PrestaShop SA
*}

{if $status == 'ok'}
    <p>
      {l s='Your order on %s is complete.' sprintf=[$shop_name] d='Modules.Wirepayment.Shop'}<br/>
      {l s='Please send us a bank wire with:' d='Modules.Wirepayment.Shop'}
    </p>
    {include file='module:ps_wirepayment/views/templates/hook/_partials/payment_infos.tpl'}

    <p>
      {l s='Podaj numer zamówienia %s w opisie przelewu.' sprintf=[$reference] d='Modules.Wirepayment.Shop'}<br/>
      {l s='Ta informacja została również wysłana na Twój e-mail.' d='Modules.Wirepayment.Shop'}
    </p>
    <strong>{l s='Zamówienie zostanie wysłane, gdy otrzymamy twój przelew.' d='Modules.Wirepayment.Shop'}</strong>
    <p>
      {l s='Jeżeli masz jakieś pytania, wątpliwości, skontaktuj się proszę z [1]działem obsługi klienta[/1].' d='Modules.Wirepayment.Shop' sprintf=['[1]' => "<a href='{$contact_url}'>", '[/1]' => '</a>']}
    </p>
{else}
    <p class="warning">
      {l s='Zauważyliśmy problem z twoim zamówieniem. Jeżeli uważasz, że to błąd, skontaktuj się z naszym [1]działem obsługi klienta[/1].' d='Modules.Wirepayment.Shop' sprintf=['[1]' => "<a href='{$contact_url}'>", '[/1]' => '</a>']}
    </p>
{/if}
