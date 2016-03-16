//
//  UICallCellDataNew.h
//  linphone
//
//  Created by Misha Torosyan on 3/15/16.
//
//

#import <Foundation/Foundation.h>
#include "linphone/linphonecore.h"

typedef enum CallCellOtherView {
    CallCellOtherView_Avatar = 0,
    CallCellOtherView_AudioStats,
    CallCellOtherView_VideoStats,
    CallCellOtherView_MAX
} CallCellOtherView;

@interface UICallCellDataNew : NSObject

@property (nonatomic, assign) BOOL minimize;
@property (nonatomic, assign) CallCellOtherView view;
@property (nonatomic, assign) LinphoneCall *call;
@property (nonatomic, strong) UIImage *image;
@property (nonatomic, strong) NSString *address;

- (id)init:(LinphoneCall*) call minimized:(BOOL)minimized;

@end
