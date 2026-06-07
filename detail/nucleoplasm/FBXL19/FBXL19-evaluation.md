---
type: protein-evaluation
gene: "FBXL19"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## FBXL19 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXL19 |
| 蛋白大小 | 694 aa |
| UniProt ID | Q6PCT2 (F-box/LRR-repeat protein 19) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL19/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL19/IF_images/SH-SY5Y_1.jpg|SH-SY5Y]]


### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | x4 | 32 | HPA 标注: Nucleoplasm |
| 📏 蛋白大小 | 10/10 | x1 | 10 | 694 aa |
| 🆕 研究新颖性 | 6/10 | x5 | 40 | PubMed 46 篇 |
| 🏗️ 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT 66.6, v6 |
| 🧬 调控结构域 | 10/10 | x2 | 20 | InterPro 10 个结构域条目 |
| 🔗 PPI 网络 | 4/10 | x3 | 12 | STRING 0 partners |
| ➕ 互证加分 | — | max +3 | +0.5 | 核候选保守蛋白基线 |
|  | **原始总分** |  | **125.5/183** | **125.0/183** |  |  |  |
|  | **归一化总分** |  | **68.6/100** | **68.3/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA | Nucleoplasm | Tier1 |
| UniProt | ,  | — |

**结论**: HPA 标注: Nucleoplasm。核定位得分 8/10。

**IF 图片**: IF image available (embedded above), see IF_images/.

#### 3.2 蛋白大小评估
- 694 aa
- 大小适宜性评分：10/10

**评价**: 694 aa 蛋白，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 46 |
| 新颖性评分 | 8/10 |

**评价**: PubMed 46 篇，属于非常新颖，少数基础研究。

**关键文献**:
1. No Authors Listed (2025). "Retraction Note". *Eur Rev Med Pharmacol Sci*. PMID: 41059755
2. Sheykhhasan M et al. (2022). "FLVCR1-AS1 and FBXL19-AS1: Two Putative lncRNA Candidates in Multiple Human Cancers". *Noncoding RNA*. PMID: 36649030
3. Zhao X et al. (2022). "Long Noncoding RNA FBXL19-AS1-Mediated Ulcerative Colitis-Associated Intestinal Epithelial Barrier Defect". *Tissue Eng Regen Med*. PMID: 36048401
4. Dong S et al. (2021). "SCF FBXW17 E3 ubiquitin ligase regulates FBXL19 stability and cell migration". *J Cell Biochem*. PMID: 33053230
5. O'Rielly DD & Rahman P (2014). "Genetics of psoriatic arthritis". *Best Pract Res Clin Rheumatol*. PMID: 25488777
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 66.6 |
| 有序区域 (pLDDT>70) 占比 | 54.4% |
| pLDDT>90 占比 | 28.0% |
| pLDDT 70-90 占比 | 26.4% |
| pLDDT 50-70 占比 | 7.1% |
| pLDDT<50 占比 | 38.6% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 查询中 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL19/FBXL19-PAE.png]]

**评价**: AlphaFold中等质量预测（pLDDT=66.6）。有高置信度折叠域，结构可信度高。评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| F-box domain | IPR |
| Zinc finger, PHD-type | IPR |
| Zinc finger, CXXC-type | IPR |
| Leucine-rich repeat, cysteine-containing subtype | IPR |
| Zinc finger, FYVE/PHD-type | IPR |
| Zinc finger, RING/FYVE/PHD-type | IPR |
| Zinc finger, PHD-type, conserved site | IPR |
| Zinc finger, PHD-finger | IPR |

**染色质调控潜力分析**: InterPro 注释了 10 个结构域条目。包含其他结构域类型。评分 10/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| 无高置信度互作伙伴 | — | — | — |

**GO-CC 复合体**: 从 UniProt GO 注释提取

**PPI 互证分析**:
- STRING 高置信度 (>0.7) partners: 0 个
- 调控相关比例: 待进一步分析

**评价**: STRING 数据库显示 0 个互作伙伴。评分 4/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT 66.6 | — |
| 结构域 | InterPro | 10 个条目 | — |
| PPI | STRING | 0 partners | — |
| 定位 | HPA / UniProt | Nucleoplasm | — |

**互证加分明细**:
- 进化保守性: 核候选保守蛋白 → +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (4.0/5)

**核心优势**:
1. 较新颖，PubMed ≤100 篇
2. AlphaFold 结构中等

**风险/不确定性**:
1. 结构质量中等
2. '研究数据有限，需更多实验验证'

**下一步建议**:
- [ ] 在 TEreg 系统中检测 FBXL19 表达及定位
- [ ] 通过 co-IP/MS 验证 PPI 网络
- [ ] ChIP-seq 检查 FBXL19 在 TE 区域的 occupancy

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PCT2
- Protein Atlas: https://www.proteinatlas.org/search/FBXL19
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PCT2
- STRING: https://string-db.org/network/9606.FBXL19
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q6PCT2/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[FBXL19-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL19/FBXL19-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6PCT2 |
| SMART | SM00256;SM00367;SM00249; |
| UniProt Domain [FT] | DOMAIN 418..464; /note="F-box" |
| InterPro | IPR001810;IPR050690;IPR006553;IPR032675;IPR019786;IPR002857;IPR011011;IPR001965;IPR019787;IPR013083; |
| Pfam | PF12937;PF16866;PF02008; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000099364-FBXL19/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MED19 | Biogrid, Opencell | true |
| MED29 | Biogrid, Opencell | true |
| PSME3 | Biogrid, Opencell | true |
| RPS11 | Opencell | false |
| SKP1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
