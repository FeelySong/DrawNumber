<%@ Page Language="C#" AutoEventWireup="true" Inherits="userbank_banklist" CodeBehind="banklist.aspx.cs" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>账户充值</title>
    <link href="../css/global.css" rel="stylesheet" type="text/css" />
    <link href="../css/right.css" rel="stylesheet" type="text/css" />
    <link href="../css/window.css" rel="stylesheet" type="text/css" />
    <link rel="stylesheet" type="text/css" href="../scripts/easyui-1.2.5/themes/default/easyui.css" />
    <link rel="stylesheet" type="text/css" href="../scripts/easyui-1.2.5/themes/icon.css" />
    <script type="text/javascript" src="../scripts/easyui-1.2.5/jquery-1.7.1.min.js"></script>
    <script type="text/javascript" src="../scripts/easyui-1.2.5/jquery.easyui.min.js"></script>
    <script src="../scripts/common.js" type="text/javascript"></script>
    <script src="../scripts/innerpage.js" type="text/javascript"></script>
    <style type="text/css">
        .copytxt
        {
            color: red;
            cursor: pointer;
        }
        .zfb
        {
            color: #ff0000;
            text-align: center;
            margin-top: -18px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
    <div class="right_01">
        <table class="right_02" border="0" cellpadding="0" cellspacing="0" width="100%">
            <tr class="right_02_01">
                <td valign="top">
                    <div class="right_02_01_01">
                    </div>
                </td>
                <td class="right_02_01_02">
                    <table width="100%" border="0" cellspacing="1">
                        <tr class="table_title">
                            <td colspan="3" style="background: none; width: 100%">
                                账户充值
                            </td>
                        </tr>
                        <tbody runat="server" id="banklist">
                            <tr class="table_content_left">
                                <td style="text-align: center; width: 20%">
                                    大额支付
                                </td>
                                <td style="width: 80%">
                                    <asp:RadioButtonList ID="ddlbanklist2" runat="server" RepeatDirection="Horizontal"
                                        CssClass="innertable">
                                    </asp:RadioButtonList>
                                </td>
                            </tr>
                            <tr class="table_content_left">
                                <td style="text-align: center;">
                                </td>
                                <td>
                                    <asp:Button ID="BtnBig" runat="server" Text="下一步" OnClick="BtnBig_Click" CssClass="btnsearch" />
                                </td>
                            </tr>
                            <tr class="table_content_left">
                                <td style="text-align: center; width: 20%">
                                    小额支付(可信用卡充值)
                                </td>
                                <td style="width: 80%">
                                    <asp:RadioButtonList ID="ddlbanklist1" runat="server" RepeatDirection="Horizontal"
                                        CssClass="innertable"  >
                                    </asp:RadioButtonList>
                                </td>
                            </tr>
                            <tr class="table_content_left">
                                <td style="text-align: center;">
                                </td>
                                <td>
                                    <asp:Button ID="BtnSmall" runat="server" Text="下一步" CssClass="btnsearch" OnClick="BtnSmall_Click"
                                         />
                                </td>
                            </tr>
                        </tbody>
                        <tbody runat="server" id="icbc">
                            <tr class="table_content_left">
                                <td style="text-align: center">
                                    支付方式
                                </td>
                                <td>
                                    <asp:Label ID="lbico" runat="server" Text="Label"></asp:Label>
                                </td>
                            </tr>
                            <tr class="table_content_left">
                                <td style="text-align: center;">
                                    账号
                                </td>
                                <td>
                                    <asp:Label ID="lbbanknum" runat="server" Text="Label"></asp:Label>&nbsp;<span onclick="copyTxt('lbbanknum')"
                                        class="copytxt">【复制】</span>
                                </td>
                            </tr>
                            <tr class="table_content_left">
                                <td style="text-align: center;">
                                    户名
                                </td>
                                <td>
                                    <asp:Label ID="lbbankaccount" runat="server" Text="Label"></asp:Label>&nbsp;<span
                                        onclick="copyTxt('lbbankaccount')" class="copytxt">【复制】</span>
                                </td>
                            </tr>
                            <tr class="table_content_left">
                                <td style="text-align: center;">
                                    附言
                                </td>
                                <td>
                                    <asp:Label ID="lbuserid" runat="server" Text="Label"></asp:Label>&nbsp;<span onclick="copyTxt('lbuserid')"
                                        class="copytxt">【复制】</span>
                                </td>
                            </tr>
                            <tr class="table_content_left">
                                <td style="text-align: center;">
                                    付款说明
                                </td>
                                <td>
                                    <asp:Label ID="lbremark" runat="server" Text="Label" ForeColor="Red"></asp:Label>
                                </td>
                            </tr>
                            <tr class="table_content_left">
                                <td style="text-align: center;">
                                    操作图例
                                </td>
                                <td>
                                    <asp:Label ID="lbopimage" runat="server" Text="Label"></asp:Label>
                                </td>
                            </tr>
                            <tr class="table_content_left">
                                <td style="text-align: center;">
                                </td>
                                <td>
                                    <asp:Button ID="Button2" runat="server" Text="上一步" CssClass="btnsearch" OnClick="Button2_Click" />
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
                <td valign="top">
                    <div class="right_02_01_03">
                    </div>
                </td>
            </tr>
            <tr>
                <td>
                </td>
                <td style="padding: 10px 0 5px 0;">
                </td>
                <td>
                </td>
            </tr>
            <tr class="right_01_26">
                <td class="right_01_29">
                </td>
                <td>
                </td>
                <td class="right_01_30">
                </td>
            </tr>
        </table>
    </div>
    </form>
</body>
</html>
<script type="text/javascript" language="javascript">
    function copyTxt(id) {
        window.clipboardData.setData('text', $("#" + id).text());
    }
</script>
