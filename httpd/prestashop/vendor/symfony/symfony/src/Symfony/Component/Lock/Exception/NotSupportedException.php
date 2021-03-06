<?php

/*
 * This file is part of the Symfony package.
 *
 * (c) Fabien Potencier <fabien@symfony.com>
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace Symfony\Component\Lock\Exception;

/**
 * NotSupportedException is thrown when an unsupported method is called.
 *
 * @author Jérémy Derussé <jeremy@derusse.com>
 */
class NotSupportedException extends \LogicException implements ExceptionInterface
{
}
