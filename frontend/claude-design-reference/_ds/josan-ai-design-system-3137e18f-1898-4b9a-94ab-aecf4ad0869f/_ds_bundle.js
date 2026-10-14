/* @ds-bundle: {"format":4,"namespace":"JosanAIDesignSystem_3137e1","components":[{"name":"Button","sourcePath":"components/buttons/Button.jsx"},{"name":"IconButton","sourcePath":"components/buttons/IconButton.jsx"},{"name":"LinkButton","sourcePath":"components/buttons/LinkButton.jsx"},{"name":"SegmentedControl","sourcePath":"components/controls/SegmentedControl.jsx"},{"name":"Badge","sourcePath":"components/data/Badge.jsx"},{"name":"Card","sourcePath":"components/data/Card.jsx"},{"name":"StatCard","sourcePath":"components/data/StatCard.jsx"},{"name":"Field","sourcePath":"components/forms/Field.jsx"},{"name":"Input","sourcePath":"components/forms/Input.jsx"},{"name":"Select","sourcePath":"components/forms/Select.jsx"},{"name":"SidePanel","sourcePath":"components/layout/SidePanel.jsx"}],"sourceHashes":{"components/buttons/Button.jsx":"a686ee5a5a91","components/buttons/IconButton.jsx":"10d2b9b999a6","components/buttons/LinkButton.jsx":"e6a6349183bd","components/controls/SegmentedControl.jsx":"19ac2b13d612","components/data/Badge.jsx":"0701cacc86fd","components/data/Card.jsx":"2fef5ed9c201","components/data/StatCard.jsx":"6dbc2386f3f2","components/forms/Field.jsx":"8df92b72c9e9","components/forms/Input.jsx":"6d70f2cb6dbf","components/forms/Select.jsx":"0adbff6b58c7","components/layout/SidePanel.jsx":"032608556557"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.JosanAIDesignSystem_3137e1 = window.JosanAIDesignSystem_3137e1 || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/buttons/Button.jsx
try { (() => {
const variantMap = {
  primary: {
    background: 'var(--accent)',
    color: '#fff',
    borderColor: 'var(--accent)'
  },
  ghost: {
    background: 'none',
    borderColor: 'transparent'
  },
  danger: {
    color: 'var(--danger)',
    borderColor: 'var(--hairline-strong)'
  },
  default: {}
};
function Button({
  variant = 'default',
  disabled,
  onClick,
  children,
  style,
  type = 'button'
}) {
  const base = {
    padding: '7px 14px',
    fontSize: '13px',
    fontFamily: 'inherit',
    borderRadius: 'var(--radius, 4px)',
    border: '1px solid var(--hairline-strong)',
    background: 'var(--surface)',
    color: 'var(--ink)',
    cursor: disabled ? 'not-allowed' : 'pointer',
    fontWeight: 500,
    display: 'inline-flex',
    alignItems: 'center',
    gap: '6px',
    opacity: disabled ? 0.5 : 1,
    lineHeight: 1,
    transition: 'background 0.1s, filter 0.1s'
  };
  return /*#__PURE__*/React.createElement("button", {
    type: type,
    style: {
      ...base,
      ...(variantMap[variant] || {}),
      ...style
    },
    disabled: disabled,
    onClick: onClick
  }, children);
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/buttons/Button.jsx", error: String((e && e.message) || e) }); }

// components/buttons/IconButton.jsx
try { (() => {
function IconButton({
  variant = 'default',
  onClick,
  children,
  style,
  title,
  'aria-label': ariaLabel
}) {
  const base = {
    width: 28,
    height: 28,
    border: '1px solid var(--hairline)',
    background: 'var(--surface)',
    borderRadius: 'var(--radius, 4px)',
    cursor: 'pointer',
    color: 'var(--muted)',
    fontSize: 12,
    display: 'inline-flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontFamily: 'inherit',
    transition: 'color 0.1s, border-color 0.1s',
    flexShrink: 0,
    ...(variant === 'ghost' ? {
      border: '1px solid transparent',
      background: 'none'
    } : {}),
    ...style
  };
  return /*#__PURE__*/React.createElement("button", {
    type: "button",
    style: base,
    onClick: onClick,
    title: title,
    "aria-label": ariaLabel
  }, children);
}
Object.assign(__ds_scope, { IconButton });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/buttons/IconButton.jsx", error: String((e && e.message) || e) }); }

// components/buttons/LinkButton.jsx
try { (() => {
function LinkButton({
  onClick,
  children,
  style
}) {
  return /*#__PURE__*/React.createElement("button", {
    type: "button",
    onClick: onClick,
    style: {
      background: 'none',
      border: 'none',
      color: 'var(--accent)',
      fontSize: '12px',
      cursor: 'pointer',
      padding: 0,
      fontFamily: 'inherit',
      textDecoration: 'none',
      ...style
    }
  }, children);
}
Object.assign(__ds_scope, { LinkButton });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/buttons/LinkButton.jsx", error: String((e && e.message) || e) }); }

// components/controls/SegmentedControl.jsx
try { (() => {
function SegmentedControl({
  options = [],
  value,
  onChange,
  size = 'default'
}) {
  const pad = size === 'sm' ? '4px 8px' : '5px 10px';
  const fs = size === 'sm' ? '11px' : '12px';
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'inline-flex',
      border: '1px solid var(--hairline)',
      borderRadius: 'var(--radius, 4px)',
      overflow: 'hidden'
    }
  }, options.map(opt => {
    const active = opt === value;
    return /*#__PURE__*/React.createElement("button", {
      key: opt,
      type: "button",
      onClick: () => onChange(opt),
      style: {
        padding: pad,
        fontSize: fs,
        background: active ? 'var(--bg)' : 'none',
        border: 'none',
        borderRight: '1px solid var(--hairline)',
        color: active ? 'var(--ink)' : 'var(--muted)',
        fontWeight: active ? 500 : 400,
        cursor: 'pointer',
        fontFamily: 'inherit',
        transition: 'background 0.1s'
      }
    }, opt);
  }));
}
Object.assign(__ds_scope, { SegmentedControl });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/controls/SegmentedControl.jsx", error: String((e && e.message) || e) }); }

// components/data/Badge.jsx
try { (() => {
function Badge({
  label,
  dot,
  dotColor,
  style
}) {
  return /*#__PURE__*/React.createElement("span", {
    style: {
      display: 'inline-flex',
      alignItems: 'center',
      gap: 6,
      padding: '4px 10px',
      border: '1px solid var(--hairline-strong)',
      borderRadius: 'var(--radius-pill, 100px)',
      fontSize: 12,
      color: 'var(--ink-soft)',
      fontFamily: 'inherit',
      ...style
    }
  }, dot && /*#__PURE__*/React.createElement("span", {
    style: {
      width: 6,
      height: 6,
      borderRadius: '50%',
      background: dotColor || 'var(--accent)',
      flexShrink: 0
    }
  }), label);
}
Object.assign(__ds_scope, { Badge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/data/Badge.jsx", error: String((e && e.message) || e) }); }

// components/data/Card.jsx
try { (() => {
function Card({
  title,
  subtitle,
  actions,
  children,
  style
}) {
  return /*#__PURE__*/React.createElement("section", {
    style: {
      background: 'var(--surface)',
      border: '1px solid var(--hairline)',
      borderRadius: 'var(--radius-lg, 6px)',
      padding: 'var(--pad-card, 20px)',
      ...style
    }
  }, (title || actions) && /*#__PURE__*/React.createElement("header", {
    style: {
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      marginBottom: 16
    }
  }, /*#__PURE__*/React.createElement("div", null, title && /*#__PURE__*/React.createElement("h3", {
    style: {
      margin: 0,
      fontSize: 14,
      fontWeight: 600
    }
  }, title), subtitle && /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 11,
      color: 'var(--muted)',
      marginTop: 2
    }
  }, subtitle)), actions && /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 8,
      alignItems: 'center'
    }
  }, actions)), children);
}
Object.assign(__ds_scope, { Card });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/data/Card.jsx", error: String((e && e.message) || e) }); }

// components/data/StatCard.jsx
try { (() => {
function Sparkline({
  data,
  color
}) {
  const W = 180,
    H = 26;
  if (!data || data.length < 2) return /*#__PURE__*/React.createElement("svg", {
    width: W,
    height: H
  });
  const max = Math.max(...data),
    min = Math.min(...data),
    span = max - min || 1;
  const step = W / (data.length - 1);
  const pts = data.map((v, i) => `${i * step},${H - (v - min) / span * (H - 2) - 1}`);
  return /*#__PURE__*/React.createElement("svg", {
    width: W,
    height: H,
    viewBox: `0 0 ${W} ${H}`,
    style: {
      display: 'block',
      marginTop: 8
    }
  }, /*#__PURE__*/React.createElement("polyline", {
    fill: "none",
    stroke: color || 'var(--accent)',
    strokeWidth: "1.25",
    points: pts.join(' '),
    strokeLinejoin: "round"
  }));
}
function StatCard({
  label,
  value,
  unit,
  delta,
  deltaDir,
  sparkData,
  color
}) {
  const deltaColor = deltaDir === 'down' ? 'var(--danger)' : deltaDir === 'up' ? 'var(--success)' : 'var(--muted)';
  return /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 11,
      color: 'var(--muted)',
      marginBottom: 6,
      letterSpacing: '0.02em'
    }
  }, label), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      alignItems: 'baseline',
      gap: 8,
      flexWrap: 'wrap'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 28,
      fontWeight: 600,
      fontFamily: 'var(--font-mono)',
      letterSpacing: '-0.02em',
      color: 'var(--ink)'
    }
  }, value), unit && /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 12,
      color: 'var(--muted)',
      fontFamily: 'var(--font-mono)'
    }
  }, unit), delta && /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 12,
      fontFamily: 'var(--font-mono)',
      color: deltaColor
    }
  }, "\xB7 ", delta)), sparkData && /*#__PURE__*/React.createElement(Sparkline, {
    data: sparkData,
    color: color
  }));
}
Object.assign(__ds_scope, { StatCard });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/data/StatCard.jsx", error: String((e && e.message) || e) }); }

// components/forms/Field.jsx
try { (() => {
function Field({
  label,
  children,
  style
}) {
  return /*#__PURE__*/React.createElement("label", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 6,
      flex: 1,
      ...style
    }
  }, label && /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 11,
      color: 'var(--muted)',
      letterSpacing: '0.02em',
      fontFamily: 'inherit'
    }
  }, label), children);
}
Object.assign(__ds_scope, { Field });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Field.jsx", error: String((e && e.message) || e) }); }

// components/forms/Input.jsx
try { (() => {
function Input({
  value,
  onChange,
  placeholder,
  type = 'text',
  affix,
  disabled,
  style,
  onFocus,
  onBlur
}) {
  const [focused, setFocus] = React.useState(false);
  const inputStyle = {
    width: '100%',
    padding: '8px 10px',
    paddingRight: affix ? 50 : 10,
    border: `1px solid ${focused ? 'var(--accent)' : 'var(--hairline-strong)'}`,
    borderRadius: 'var(--radius, 4px)',
    background: 'var(--surface)',
    color: 'var(--ink)',
    fontSize: '13px',
    outline: 'none',
    fontFamily: 'inherit',
    transition: 'border-color 0.1s',
    ...(disabled ? {
      opacity: 0.5,
      cursor: 'not-allowed'
    } : {}),
    ...style
  };
  return /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'relative',
      display: 'flex',
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("input", {
    type: type,
    value: value,
    onChange: onChange,
    placeholder: placeholder,
    disabled: disabled,
    style: inputStyle,
    onFocus: e => {
      setFocus(true);
      onFocus?.(e);
    },
    onBlur: e => {
      setFocus(false);
      onBlur?.(e);
    }
  }), affix && /*#__PURE__*/React.createElement("span", {
    style: {
      position: 'absolute',
      right: 10,
      fontSize: 11,
      color: 'var(--muted)',
      fontFamily: 'var(--font-mono)',
      pointerEvents: 'none'
    }
  }, affix));
}
Object.assign(__ds_scope, { Input });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Input.jsx", error: String((e && e.message) || e) }); }

// components/forms/Select.jsx
try { (() => {
function Select({
  value,
  onChange,
  options = [],
  disabled,
  style
}) {
  return /*#__PURE__*/React.createElement("select", {
    value: value,
    onChange: onChange,
    disabled: disabled,
    style: {
      width: '100%',
      padding: '8px 10px',
      border: '1px solid var(--hairline-strong)',
      borderRadius: 'var(--radius, 4px)',
      background: 'var(--surface)',
      color: 'var(--ink)',
      fontSize: '13px',
      outline: 'none',
      fontFamily: 'inherit',
      cursor: 'pointer',
      ...(disabled ? {
        opacity: 0.5,
        cursor: 'not-allowed'
      } : {}),
      ...style
    }
  }, options.map(opt => /*#__PURE__*/React.createElement("option", {
    key: typeof opt === 'string' ? opt : opt.value,
    value: typeof opt === 'string' ? opt : opt.value
  }, typeof opt === 'string' ? opt : opt.label)));
}
Object.assign(__ds_scope, { Select });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Select.jsx", error: String((e && e.message) || e) }); }

// components/layout/SidePanel.jsx
try { (() => {
function SidePanel({
  open,
  onClose,
  title,
  subtitle,
  children,
  footer,
  style
}) {
  return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("div", {
    onClick: onClose,
    style: {
      position: 'fixed',
      inset: 0,
      background: 'rgba(0,0,0,0.15)',
      opacity: open ? 1 : 0,
      pointerEvents: open ? 'auto' : 'none',
      transition: 'opacity 0.18s ease',
      zIndex: 40
    }
  }), /*#__PURE__*/React.createElement("aside", {
    style: {
      position: 'fixed',
      top: 0,
      right: 0,
      width: 'var(--sidepanel-w, 440px)',
      maxWidth: '94vw',
      height: '100vh',
      background: 'var(--surface)',
      borderLeft: '1px solid var(--hairline)',
      transform: open ? 'translateX(0)' : 'translateX(100%)',
      transition: 'transform 0.22s cubic-bezier(0.2,0.8,0.2,1)',
      zIndex: 50,
      display: 'flex',
      flexDirection: 'column',
      ...style
    }
  }, /*#__PURE__*/React.createElement("header", {
    style: {
      padding: '18px 22px',
      borderBottom: '1px solid var(--hairline)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      flexShrink: 0
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 12,
      fontWeight: 600,
      letterSpacing: '0.02em'
    }
  }, title), subtitle && /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 11,
      color: 'var(--muted)',
      marginTop: 2
    }
  }, subtitle)), /*#__PURE__*/React.createElement("button", {
    type: "button",
    onClick: onClose,
    "aria-label": "Close",
    style: {
      width: 28,
      height: 28,
      border: '1px solid var(--hairline)',
      background: 'var(--surface)',
      borderRadius: 'var(--radius, 4px)',
      cursor: 'pointer',
      color: 'var(--muted)',
      fontSize: 12,
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center'
    }
  }, "\u2715")), /*#__PURE__*/React.createElement("div", {
    style: {
      flex: 1,
      overflowY: 'auto',
      padding: '20px 22px',
      display: 'flex',
      flexDirection: 'column',
      gap: 16
    }
  }, children), footer && /*#__PURE__*/React.createElement("footer", {
    style: {
      padding: '16px 22px',
      borderTop: '1px solid var(--hairline)',
      display: 'flex',
      alignItems: 'center',
      gap: 8,
      flexShrink: 0
    }
  }, footer)));
}
Object.assign(__ds_scope, { SidePanel });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/layout/SidePanel.jsx", error: String((e && e.message) || e) }); }

__ds_ns.Button = __ds_scope.Button;

__ds_ns.IconButton = __ds_scope.IconButton;

__ds_ns.LinkButton = __ds_scope.LinkButton;

__ds_ns.SegmentedControl = __ds_scope.SegmentedControl;

__ds_ns.Badge = __ds_scope.Badge;

__ds_ns.Card = __ds_scope.Card;

__ds_ns.StatCard = __ds_scope.StatCard;

__ds_ns.Field = __ds_scope.Field;

__ds_ns.Input = __ds_scope.Input;

__ds_ns.Select = __ds_scope.Select;

__ds_ns.SidePanel = __ds_scope.SidePanel;

})();
