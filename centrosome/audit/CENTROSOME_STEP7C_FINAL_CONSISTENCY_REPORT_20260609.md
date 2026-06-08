# Centrosome Module Step 7C — 最终一致性报告

**日期:** 2026-06-09
**Step 7B commit:** `e373205a`

---

## 1. 716 / 711 / 701 差异解释

| 数值 | 含义 | 说明 |
|:---:|------|------|
| **716** | HPA 种子基因总数 | Centrosome(513) + Satellite(228) − Both(25) |
| **711** | 已评估报告数 | 716 − 5 个 PubMed 查询失败基因 |
| **701** | Step 7B 再生数 | 711 − 10 个 pilot 基因（人工撰写，排除再生） |

### 5 个缺失种子基因

PubMed eutils API 查询失败（SSL EOF 错误），无法获取文献计数，因此未进行评估：

| Gene | 原因 |
|------|------|
| ANP32D | PubMed query failed |
| PIK3C2G | PubMed query failed |
| PRKAR2B | PubMed query failed |
| SDCCAG8 | PubMed query failed |
| ZNF322 | PubMed query failed |

这5个基因需要手动重试 PubMed 查询后补评估。

### 10 个未再生报告（Pilot）

Pilot 10 为人工撰写的详细评估报告，排除在 Step 7B 自动再生之外：

| Gene | 状态 | 语言 | 备注 |
|------|------|:---:|------|
| AURKA | ELIMINATED | EN | 人工撰写，含详细生物学分析 |
| PLK4 | ELIMINATED | EN | 人工撰写 |
| CEP192 | ELIMINATED | EN | 人工撰写 |
| CETN2 | ELIMINATED | EN | 人工撰写 |
| PCM1 | ELIMINATED | EN | 人工撰写 |
| CCP110 | CANDIDATE | EN | 人工撰写 |
| NEDD1 | CANDIDATE | EN | 人工撰写 |
| CEP72 | CANDIDATE | EN | 人工撰写 |
| CEP97 | CANDIDATE | EN | 人工撰写 |
| CCDC14 | MANUAL_REVIEW | EN | 人工撰写 |

---

## 2. 核心统计

| 指标 | 数量 |
|------|:---:|
| HPA 种子基因 | 716 |
| 已评估报告 | 711 |
| 索引记录 | 711 |
| Docs HTML 页面 | 711 |
| Step 7B 再生 | 701 |
| 缺失种子 | 5 |
| 未再生但有效 | 10 (pilot) |
| 真正未解决 | 5 (PubMed 查询失败) |

### 状态分布

| 状态 | 数量 |
|------|:---:|
| CENTROSOME_CANDIDATE | 441 |
| CENTROSOME_ELIMINATED | 255 |
| CENTROSOME_LOW_PRIORITY | 14 |
| CENTROSOME_MANUAL_REVIEW | 1 |

---

## 3. 报告质量

| 检查项 | 预期 | 实际 | 状态 |
|--------|:---:|:---:|:---:|
| TE module remaining | 0 | 10 (pilot) | ⚠️ 已知 |
| PPI Pending remaining | 0 | 0 | ✅ |
| Nuclear rejection logic | 0 | 0 | ✅ |
| Five-dimension scoring | 701 | 701 | ✅ |
| Chinese reports | 701 | 701 | ✅ |
| Non-Chinese reports | 10 (pilot) | 10 | ⚠️ 已知 |
| PAE missing explained | — | 451 | ✅ |

> **说明**: 10 个 pilot 报告含 TE 模块且为英文，这是 Step 7B 主动排除的结果。Pilot 报告为人工撰写，保留详细生物学分析内容。701 个自动再生报告全部中文、五维度评分、含 STRING PPI 数据。

---

## 4. IF 图像显示

| 指标 | 数量 |
|------|:---:|
| HPA 外部图像 URL 嵌入 | 446 |
| Markdown `![]()` 嵌入 | 446 |
| HTML 可解析图像 | 446 |
| 无图像（淘汰报告） | 265 |
| 损坏的本地引用 | 0 |
| **broken image count** | **0** |

---

## 5. 主 atlas 完整性

| 检查项 | 预期 | 实际 | 状态 |
|--------|:---:|:---:|:---:|
| `protein_report_index.json` records | 5,647 | 5,647 | ✅ |
| `protein_report_index.tsv` lines | 5,648 | 5,648 | ✅ |
| `detail/` evaluation reports | 5,647 | 5,647 | ✅ |
| `docs/reports/` HTML pages | 5,647 | 5,647 | ✅ |
| `docs/category/` pages | 8 | 8 | ✅ |
| Centrosome in main `detail/` | 0 | 0 | ✅ |
| Centrosome in main `docs/reports/` | 0 | 0 | ✅ |
| `protein-finding.md` centrosome mention | 0 | 0 | ✅ |
| Main `docs/index.html` stats preserved | Yes | Yes | ✅ |

**结论: ✅ Main atlas NOT polluted.**

---

## 6. 网页索引

| 检查项 | 状态 |
|--------|:---:|
| `docs/centrosome/index.html` | ✅ |
| `docs/centrosome/protein_index.html` | ✅ |
| `docs/centrosome/data/centrosome_report_index.json` | ✅ |
| 搜索/筛选 JS | ✅ |
| 排序 JS | ✅ |
| 索引→报告链接全部有效 | ✅ (0 broken) |
| 主首页 centrosome 入口 | ✅ |

---

## 7. 最终决策

**ACCEPT_CENTROSOME_MODULE_WITH_KNOWN_SEED_BACKLOG**

### 判定依据:

- ✅ main atlas changed? **NO**
- ✅ broken image count: **0**
- ✅ PPI Pending remaining (auto-generated): **0**
- ✅ nuclear rejection logic: **0**
- ✅ 711 评估/索引/docs 一致
- ✅ 5 缺失种子有明确原因（PubMed API 查询失败）
- ⚠️ 10 pilot 报告含 TE 模块/英文（已知且主动保留）

### 后续建议:

1. **5 个缺失种子**: 重试 PubMed 查询（可能与网络或 API rate limit 有关），补评估
2. **10 个 pilot 报告**: 可选是否翻译为中文并移除 TE 模块，当前保留人工撰写质量
3. **455 个候选报告**: UniProt/GO-CC、PDB/结构域、IntAct/BioGRID 数据标注为"待人工补充"，后续可分批完善
4. **GitHub Pages**: `docs/centrosome/` 已就绪，可部署

### Safe to proceed: ✅ YES
