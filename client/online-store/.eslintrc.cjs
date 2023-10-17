module.exports = {
  extends: '@antfu',
  rules: {
    'arrow-body-style': ['error', 'always'],
    'curly': 'error',
    'vue/no-reserved-component-names': ['warn', {
      disallowVueBuiltInComponents: false,
      disallowVue3BuiltInComponents: false,
    }],
  },

}
