import json
from dataclasses import dataclass
from typing import List, Dict

from typing import List, TypedDict

class NStyle(TypedDict):
    name: str
    value: str

styles: List[NStyle]


@dataclass
class Style:
    alignContent: str = None
    alignItems: str = None
    alignSelf: str = None
    all: str = None
    animation: str = None
    animationDelay: str = None
    animationDirection: str = None
    animationDuration: str = None
    animationFillMode: str = None
    animationIterationCount: str = None
    animationName: str = None
    animationPlayState: str = None
    animationTimingFunction: str = None
    backfaceVisibility: str = None
    background: str = None
    backgroundAttachment: str = None
    backgroundBlendMode: str = None
    backgroundClip: str = None
    backgroundColor: str = None
    backgroundImage: str = None
    backgroundOrigin: str = None
    backgroundPosition: str = None
    backgroundRepeat: str = None
    backgroundSize: str = None
    blockSize: str = None
    border: str = None
    borderBlock: str = None
    borderBlockColor: str = None
    borderBlockEnd: str = None
    borderBlockEndColor: str = None
    borderBlockEndStyle: str = None
    borderBlockEndWidth: str = None
    borderBlockStart: str = None
    borderBlockStartColor: str = None
    borderBlockStartStyle: str = None
    borderBlockStartWidth: str = None
    borderBlockStyle: str = None
    borderBlockWidth: str = None
    borderBottom: str = None
    borderBottomColor: str = None
    borderBottomLeftRadius: str = None
    borderBottomRightRadius: str = None
    borderBottomStyle: str = None
    borderBottomWidth: str = None
    borderCollapse: str = None
    borderColor: str = None
    borderEndEndRadius: str = None
    borderEndStartRadius: str = None
    borderImage: str = None
    borderImageOutset: str = None
    borderImageRepeat: str = None
    borderImageSlice: str = None
    borderImageSource: str = None
    borderImageWidth: str = None
    borderInline: str = None
    borderInlineColor: str = None
    borderInlineEnd: str = None
    borderInlineEndColor: str = None
    borderInlineEndStyle: str = None
    borderInlineEndWidth: str = None
    borderInlineStart: str = None
    borderInlineStartColor: str = None
    borderInlineStartStyle: str = None
    borderInlineStartWidth: str = None
    borderInlineStyle: str = None
    borderInlineWidth: str = None
    borderLeft: str = None
    borderLeftColor: str = None
    borderLeftStyle: str = None
    borderLeftWidth: str = None
    borderRadius: str = None
    borderRight: str = None
    borderRightColor: str = None
    borderRightStyle: str = None
    borderRightWidth: str = None
    borderSpacing: str = None
    borderStartEndRadius: str = None
    borderStartStartRadius: str = None
    borderStyle: str = None
    borderTop: str = None
    borderTopColor: str = None
    borderTopLeftRadius: str = None
    borderTopRightRadius: str = None
    borderTopStyle: str = None
    borderTopWidth: str = None
    borderWidth: str = None
    bottom: str = None
    boxDecorationBreak: str = None
    boxShadow: str = None
    boxSizing: str = None
    breakAfter: str = None
    breakBefore: str = None
    breakInside: str = None
    captionSide: str = None
    caretColor: str = None
    clear: str = None
    clip: str = None
    color: str = None
    columnCount: str = None
    columnFill: str = None
    columnGap: str = None
    columnRule: str = None
    columnRuleColor: str = None
    columnRuleStyle: str = None
    columnRuleWidth: str = None
    columnSpan: str = None
    columnWidth: str = None
    columns: str = None
    content: str = None
    counterIncrement: str = None
    counterReset: str = None
    cursor: str = None
    direction: str = None
    display: str = None
    emptyCells: str = None
    filter: str = None
    flex: str = None
    flexBasis: str = None
    flexDirection: str = None
    flexFlow: str = None
    flexGrow: str = None
    flexShrink: str = None
    flexWrap: str = None
    float: str = None
    font: str = None
    fontFamily: str = None
    fontFeatureSettings: str = None
    fontKerning: str = None
    fontLanguageOverride: str = None
    fontOpticalSizing: str = None
    fontSize: str = None
    fontSizeAdjust: str = None
    fontStretch: str = None
    fontStyle: str = None
    fontSynthesis: str = None
    fontVariant: str = None
    fontVariantAlternates: str = None
    fontVariantCaps: str = None
    fontVariantEastAsian: str = None
    fontVariantLigatures: str = None
    fontVariantNumeric: str = None
    fontVariantPosition: str = None
    fontWeight: str = None
    gap: str = None
    grid: str = None
    gridArea: str = None
    gridAutoColumns: str = None
    gridAutoFlow: str = None
    gridAutoRows: str = None
    gridColumn: str = None
    gridColumnEnd: str = None
    gridColumnStart: str = None
    gridRow: str = None
    gridRowEnd: str = None
    gridRowStart: str = None
    gridTemplate: str = None
    gridTemplateAreas: str = None
    gridTemplateColumns: str = None
    gridTemplateRows: str = None
    hangingPunctuation: str = None
    height: str = None
    hyphens: str = None
    imageOrientation: str = None
    imageRendering: str = None
    imageResolution: str = None
    imeMode: str = None
    initialLetter: str = None
    initialLetterAlign: str = None
    inlineSize: str = None
    inset: str = None
    insetBlock: str = None
    insetBlockEnd: str = None
    insetBlockStart: str = None
    insetInline: str = None
    insetInlineEnd: str = None
    insetInlineStart: str = None
    isolation: str = None
    justifyContent: str = None
    justifyItems: str = None
    justifySelf: str = None
    left: str = None
    letterSpacing: str = None
    lineBreak: str = None
    lineHeight: str = None
    listStyle: str = None
    listStyleImage: str = None
    listStylePosition: str = None
    listStyleType: str = None
    margin: str = None
    marginBlock: str = None
    marginBlockEnd: str = None
    marginBlockStart: str = None
    marginBottom: str = None
    marginInline: str = None
    marginInlineEnd: str = None
    marginInlineStart: str = None
    marginLeft: str = None
    marginRight: str = None
    marginTop: str = None
    mask: str = None
    maskClip: str = None
    maskComposite: str = None
    maskImage: str = None
    maskMode: str = None
    maskOrigin: str = None
    maskPosition: str = None
    maskRepeat: str = None
    maskSize: str = None
    maskType: str = None
    maxBlockSize: str = None
    maxHeight: str = None
    maxInlineSize: str = None
    maxWidth: str = None
    minBlockSize: str = None
    minHeight: str = None
    minInlineSize: str = None
    minWidth: str = None
    mixBlendMode: str = None
    objectFit: str = None
    objectPosition: str = None
    offset: str = None
    offsetAnchor: str = None
    offsetBlock: str = None
    offsetBlockEnd: str = None
    offsetBlockStart: str = None
    offsetDistance: str = None
    offsetInline: str = None
    offsetInlineEnd: str = None
    offsetInlineStart: str = None
    offsetPath: str = None
    offsetPosition: str = None
    offsetRotate: str = None
    opacity: str = None
    order: str = None
    orphans: str = None
    outline: str = None
    outlineColor: str = None
    outlineOffset: str = None
    outlineStyle: str = None
    outlineWidth: str = None
    overflow: str = None
    overflowAnchor: str = None
    overflowBlock: str = None
    overflowInline: str = None
    overflowWrap: str = None
    overflowX: str = None
    overflowY: str = None
    overscrollBehavior: str = None
    overscrollBehaviorBlock: str = None
    overscrollBehaviorInline: str = None
    overscrollBehaviorX: str = None
    overscrollBehaviorY: str = None
    padding: str = None
    paddingBlock: str = None
    paddingBlockEnd: str = None
    paddingBlockStart: str = None
    paddingBottom: str = None
    paddingInline: str = None
    paddingInlineEnd: str = None
    paddingInlineStart: str = None
    paddingLeft: str = None
    paddingRight: str = None
    paddingTop: str = None
    pageBreakAfter: str = None
    pageBreakBefore: str = None
    pageBreakInside: str = None
    paintOrder: str = None
    perspective: str = None
    perspectiveOrigin: str = None
    placeContent: str = None
    placeItems: str = None
    placeSelf: str = None
    pointerEvents: str = None
    position: str = None
    quotes: str = None
    resize: str = None
    right: str = None
    rotate: str = None
    rowGap: str = None
    rubyAlign: str = None
    rubyMerge: str = None
    rubyPosition: str = None
    scale: str = None
    scrollBehavior: str = None
    scrollMargin: str = None
    scrollMarginBlock: str = None
    scrollMarginBlockEnd: str = None
    scrollMarginBlockStart: str = None
    scrollMarginBottom: str = None
    scrollMarginInline: str = None
    scrollMarginInlineEnd: str = None
    scrollMarginInlineStart: str = None
    scrollMarginLeft: str = None
    scrollMarginRight: str = None
    scrollMarginTop: str = None
    scrollPadding: str = None
    scrollPaddingBlock: str = None
    scrollPaddingBlockEnd: str = None
    scrollPaddingBlockStart: str = None
    scrollPaddingBottom: str = None
    scrollPaddingInline: str = None
    scrollPaddingInlineEnd: str = None
    scrollPaddingInlineStart: str = None
    scrollPaddingLeft: str = None
    scrollPaddingRight: str = None
    scrollPaddingTop: str = None
    scrollSnapAlign: str = None
    scrollSnapStop: str = None
    scrollSnapType: str = None
    shapeImageThreshold: str = None
    shapeMargin: str = None
    shapeOutside: str = None
    tabSize: str = None
    tableLayout: str = None
    textAlign: str = None
    textAlignLast: str = None
    textCombineUpright: str = None
    textDecoration: str = None
    textDecorationColor: str = None
    textDecorationLine: str = None
    textDecorationSkipInk: str = None
    textDecorationStyle: str = None
    textDecorationThickness: str = None
    textEmphasis: str = None
    textEmphasisColor: str = None
    textEmphasisPosition: str = None
    textEmphasisStyle: str = None
    textIndent: str = None
    textJustify: str = None
    textOrientation: str = None
    textOverflow: str = None
    textRendering: str = None
    textShadow: str = None
    textSizeAdjust: str = None
    textTransform: str = None
    textUnderlineOffset: str = None
    textUnderlinePosition: str = None
    top: str = None
    touchAction: str = None
    transform: str = None
    transformBox: str = None
    transformOrigin: str = None
    transformStyle: str = None
    transition: str = None
    transitionDelay: str = None
    transitionDuration: str = None
    transitionProperty: str = None
    transitionTimingFunction: str = None
    unicodeBidi: str = None
    userSelect: str = None
    verticalAlign: str = None
    visibility: str = None
    whiteSpace: str = None
    widows: str = None
    width: str = None
    willChange: str = None
    wordBreak: str = None
    wordSpacing: str = None
    writingMode: str = None
    zIndex: str = None


    def css(self) -> Dict[str, str]:
        style_dict = {}
        for field_name, field_value in self.__dict__.items():
            if field_value is not None:
                style_dict[field_name] = field_value
        return style_dict
    




        

        
