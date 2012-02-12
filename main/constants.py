BASE_QUESTION_TEMPLATE = """
<div class="clearfix">
  <label>{{text}}</label>
  <div class="input">
    <input type="input" name="{{id}}" />
  </div>
</div>
"""

MULTIPLE_CHOICE_TEMPLATE = """
  <label>{{text}}</label>
  <select name="{{id}}">
    {% for o in choices %}
       <option value="{{o}}">{{o}}</option>
    {% endfor %}
  </select>
"""


BOOLEAN_QUESTION_TEMPLATE = """
   <label>{{text}}</label>
   <input type="checkbox" name="{{id}}" />
"""
