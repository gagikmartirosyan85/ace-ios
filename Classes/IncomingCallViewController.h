/* IncomingCallViewController.h
 *
 * Copyright (C) 2012  Belledonne Comunications, Grenoble, France
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or   
 *  (at your option) any later version.                                 
 *                                                                      
 *  This program is distributed in the hope that it will be useful,     
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of      
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the       
 *  GNU General Public License for more details.                
 *                                                                      
 *  You should have received a copy of the GNU General Public License   
 *  along with this program; if not, write to the Free Software         
 *  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 */    

#import <UIKit/UIKit.h>

#import "UIModalViewController.h"

#include "linphonecore.h"

typedef enum _IncomingCallStates {
    IncomingCall_Accepted,
    IncomingCall_Decline,
    IncomingCall_Aborted
} IncomingCallStats;

@interface IncomingCallViewController : UIModalViewController {
@private
    UILabel* addressLabel;
    UIImageView* avatarImage;
    LinphoneCall *call;
}

@property (nonatomic, retain) IBOutlet UILabel* addressLabel;
@property (nonatomic, retain) IBOutlet UIImageView* avatarImage;

- (IBAction)onAcceptClick:(id) event;
- (IBAction)onDeclineClick:(id) event;

- (void)update:(LinphoneCall*)call;

- (LinphoneCall*) getCall;

@end
