# 07 修 HPA/IF 语义一致性：HPA IF Consistency Repair

你是 Claude Code 中的 protein-scout HPA/IF 一致性修复 agent。当前任务不是继续新蛋白，也不是重新评估所有维度，而是修复“图片已存在/已嵌入，但报告仍写暂无数据、Pending cell analysis、IF unavailable”的矛盾。

## 路径

项目路径：
`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested`

## 问题定义

以下情况必须修复：

- gene 目录中存在 `IF_images/*.jpg` 或 `IF_images/*.png`，但报告仍写：
  - `Pending cell analysis`
  - `暂无数据（Pending cell analysis）`
  - `IF unavailable`
  - `HPA 暂无 IF 原图数据`
  - `HPA 无 IF 数据`
  - `HPA IF 原图未可靠获取`
- 报告已嵌入 IF 图像，但同一报告仍写无 IF / 暂无 IF / unavailable。
- 报告写 `Protein Atlas (IF) | 暂无数据`，但同报告或本地目录已有 HPA IF 图。
- HPA reliability/main/additional 已有定位结论，但 IF 状态段仍说无法获取且没有解释图像层级。

典型错误：

```markdown
| Protein Atlas (IF) | 暂无数据（Pending cell analysis），核定位基于 UniProt | — |

![[Projects/TEreg-finding/protein-interested/detail/chromatin/CENPH/IF_images/A-431_1.jpg]]
```

这种不是缺图，而是报告语义没有同步。

## 审计阶段

先生成新的：
`audit_work/hpa_if_consistency_audit_YYYYMMDD_HHMMSS.tsv`

字段：

| gene | category | report_path | local_if_count | embedded_if_count | stale_claims | hpa_table_line | hpa_status_line | risk | action |
|---|---|---|---:|---:|---|---|---|---|---|

标记 HIGH：

- `local_if_count > 0` 且存在 stale claims。
- `embedded_if_count > 0` 且存在 stale claims。
- HPA 表格写暂无数据，但报告其他位置嵌入 IF 图。

标记 MED：

- 无本地图，但 HPA 定位文本存在，报告没有写 reliability/main/additional。
- 只有 thumbnail，报告写法没有标注 thumbnail。

## 修复阶段

只修 HIGH 前 50 个，除非用户给出更大上限。

对每个 gene：

1. 统计本地 `IF_images/` 图像。
2. 统计报告中已嵌入的 IF 图像。
3. 找到所有 stale claims。
4. 如果有本地或已嵌入 IF 图，必须把所有 HPA/IF 相关段落统一为真实状态。
5. 更新 `Protein Atlas (IF)` 表格行，不得继续写 `暂无数据/Pending/IF unavailable`。
6. 更新 `HPA IF 状态` 段。
7. 保留 HPA reliability/main/additional 和 cell line 信息。
8. 如果只是 thumbnail，写 `thumbnail only`，但不要写 `暂无数据`。
9. 如果确实没有图，才允许保留暂无数据；同时必须写已检查的来源和候选数量。

## 推荐写法

有 red_green / blue_red_green 图：

```markdown
| Protein Atlas (IF) | 已获取 HPA IF 图像；定位结论见 HPA reliability/main/additional | HPA IF image embedded |

**HPA IF 状态**: IF image available and embedded. 已嵌入本地 HPA IF 图像；核定位判断结合 HPA localization/reliability、UniProt 与 GO-CC。
```

只有 thumbnail：

```markdown
| Protein Atlas (IF) | 仅获取 thumbnail/medium 图像，已嵌入但定位证据保守使用 | thumbnail/medium embedded |
```

确实无图：

```markdown
| Protein Atlas (IF) | 暂无可用 IF 图像；已检查 HPA gene page、subcellular page、本地 IF_images 与 harvest packet | no image candidates |
```

## 禁止

- 禁止只嵌图不改旧文字。
- 禁止一个报告同时写 `IF unavailable` 和嵌入 IF 图。
- 禁止把有本地图的报告继续标为 `Pending cell analysis`。
- 禁止批量删除 HPA 段落。
- 禁止改动评分或分类，除非 HPA/IF 证据变化明确影响评分；若改分，必须跑 targeted strict。
- 禁止继续新蛋白。

## 检查

每个 gene 修复后运行：

```bash
python3 validate_strict.py --gene <GENE>
```

并运行一致性 grep：

```bash
rg "Pending cell analysis|暂无数据（Pending cell analysis）|IF unavailable|HPA 暂无 IF 原图数据|HPA 无 IF 数据|HPA IF 原图未可靠获取" detail/*/<GENE>/<GENE>-evaluation.md
```

如果 grep 仍命中，但确实无图，必须在 log 中说明 `genuine_absence: yes`，并写明 local_if_count=0、embedded_if_count=0、checked sources。

每 25 个 gene 运行：

```bash
python3 validate_strict.py --all
```

## 修复后再审计

本批完成后必须重新生成：
`audit_work/hpa_if_consistency_audit_YYYYMMDD_HHMMSS.tsv`

并确认 HIGH 数下降。若 HIGH 没下降，停止。

## Log

创建：
`log/claude_hpa_if_consistency_repair_YYYYMMDD_HHMMSS.md`

记录：

- audit 路径
- 修复 genes
- 每个 gene 的 local_if_count
- embedded_if_count
- stale claims removed
- 是否 genuine absence
- validate result
- 修复后 HIGH 数

## 完成后只输出

- 输入 audit 路径
- 修复后 audit 路径
- log 路径
- 修复 genes
- 仍有 HIGH 的 genes
- validate_strict 结果
