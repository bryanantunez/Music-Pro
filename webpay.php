<?php
error_reporting(E_ALL);
ini_set('display_errors', '1');
include 'vendor/autoload.php';

use Transbank\Webpay\WebpayPlus\Transaction;

$baseurl = "https://". $_SERVER['HTTP_HOST'] . $_SERVER['PHP_SELF'];

Transbank\Webpay\WebpayPlus::setCommerceCode('597055555532');
Transbank\Webpay\WebpayPlus::setApiKey('579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C');
Transbank\Webpay\WebpayPlus::setIntegrationType('TEST');

$action = isset($_GET["action"]) ? $_GET['action'] : 'init';
$post_array = false;
switch ($action) {

    default:

    $buy_order=rand();
    $session_id=rand();
    $amount=15000;
    $return_url = $baseurl."action=getResult";

    $response = Transaction::create($buy_order, $session_id, $amount, $return_url);

    echo "<pre>";print_r($response);echo "</pre>"
    $url_tbk = $response->url;
    $token = $response->token;
    break;

    case "getResult":
        if (!isset($_POST["token_ws"]))
        break;

        /**Token de la transacción */
        $token = filter_input(INPUT_POST, 'token_ws');

        $request = array(
            "token" => filter_input(INPUT_POST, 'token_ws")
        );

        $response = Transaction::commit($token);

        echo "<pre>";print_r($response);echo "</pre>";

        $url_tbk = $baseurl."?action=getStatus";

        break;

        case "getResult":
            if (!isset($_POST["token_ws"]))
            break;

        /**Token de la transacción*/
            $token = filter_input(INPUT_POST, 'token_ws');
    
            $request = array(
                "token" => filter_input(INPUT_POST, 'token_ws")
            );
    
            $response = Transaction::commit($token);
    
            echo "<pre>";print_r($response);echo "</pre>";
    
            $url_tbk = $baseurl."?action=getStatus";
    
            break;
}
?>