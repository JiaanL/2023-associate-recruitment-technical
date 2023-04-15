select
  o.owner_id,
  o.owner_name,
  count(distinct category_id) as different_category_count
from category_article_mapping c 
  right join article a on a.article_id = c.article_id
  right join owner o on o.owner_id = a.owner_id
  inner join category cy on cy.category_id = c.category_id
group by owner_id
order by count(distinct category_id) desc
