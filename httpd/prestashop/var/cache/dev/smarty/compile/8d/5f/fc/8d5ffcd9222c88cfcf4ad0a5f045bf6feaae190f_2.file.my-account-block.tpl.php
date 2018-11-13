<?php
/* Smarty version 3.1.32, created on 2018-11-13 16:21:14
  from '/var/www/html/modules/revws/views/templates/front/my-account-block.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.32',
  'unifunc' => 'content_5beaebea033664_42112529',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '8d5ffcd9222c88cfcf4ad0a5f045bf6feaae190f' => 
    array (
      0 => '/var/www/html/modules/revws/views/templates/front/my-account-block.tpl',
      1 => 1542119307,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5beaebea033664_42112529 (Smarty_Internal_Template $_smarty_tpl) {
?><li>
  <a id="revws-link" href="<?php echo htmlspecialchars(call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['link']->value->getModuleLink('revws','MyReviews',array(),true),'html','UTF-8' )), ENT_QUOTES, 'UTF-8');?>
">
    <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'My reviews','mod'=>'revws'),$_smarty_tpl ) );?>

  </a>
</li>
<?php }
}
