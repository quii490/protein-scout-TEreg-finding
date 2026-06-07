---
type: protein-evaluation
gene: "FBXL4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## FBXL4 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXL4 |
| 蛋白大小 | 621 aa |
| UniProt ID | Q9UKA2 (F-box/LRR-repeat protein 4) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL4/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL4/IF_images/U-251MG_1.jpg|U-251MG]]


### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | x4 | 28 | 暂无数据（HPA IF 图像已本地嵌入。

| 📏 蛋白大小 | 10/10 | x1 | 10 | 621 aa |
| 🆕 研究新颖性 | 6/10 | x5 | 30 | PubMed 56 篇 |
| 🏗️ 三维结构 | 8/10 | x3 | 24 | AlphaFold pLDDT 86.3, v6 |
| 🧬 调控结构域 | 7/10 | x2 | 14 | InterPro 5 个结构域条目 |
| 🔗 PPI 网络 | 4/10 | x3 | 12 | STRING 0 partners |
| ➕ 互证加分 | — | max +3 | +0.5 | 核候选保守蛋白基线 |
| **原始总分** |  |  | **118.5/183** |  |
| **归一化总分** |  |  | **64.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA | 暂无数据 | Tier1 |
| UniProt | , ,  | — |

**结论**: 暂无数据（HPA IF 图像已本地嵌入。


#### 3.2 蛋白大小评估
- 621 aa
- 大小适宜性评分：10/10

**评价**: 621 aa 蛋白，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 56 |
| 新颖性评分 | 6/10 |

**评价**: PubMed 56 篇，属于有一定研究但 niche 空间充足。

**关键文献**:
1. Abudureyimu M et al. (2024). "FBXL4 protects against HFpEF through Drp1-Mediated regulation of mitochondrial dynamics and the downstream SERCA2a". *Redox Biol*. PMID: 38359748
2. Cao Y et al. (2023). "A mitochondrial SCF-FBXL4 ubiquitin E3 ligase complex degrades BNIP3 and NIX to restrain mitophagy and prevent mitochondrial disease". *EMBO J*. PMID: 36896912
3. Sun Y et al. (2024). "A mitophagy sensor PPTC7 controls BNIP3 and NIX degradation to regulate mitochondrial mass". *Mol Cell*. PMID: 38151018
4. Chen Y et al. (2023). "FBXL4 mutations cause excessive mitophagy via BNIP3/BNIP3L accumulation leading to mitochondrial DNA depletion syndrome". *Cell Death Differ*. PMID: 37568009
5. Adam MP et al. (1993). "Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview". **. PMID: 26425749
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 86.3 |
| 有序区域 (pLDDT>70) 占比 | 84.6% |
| pLDDT>90 占比 | 75.7% |
| pLDDT 70-90 占比 | 8.9% |
| pLDDT 50-70 占比 | 1.8% |
| pLDDT<50 占比 | 13.7% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 查询中 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL4/FBXL4-PAE.png]]

**评价**: AlphaFold高质量预测（pLDDT=86.3）。有高置信度折叠域，结构可信度高。评分 8/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| F-box domain | IPR |
| Leucine-rich repeat, cysteine-containing subtype | IPR |
| Leucine-rich repeat domain superfamily | IPR |
| F-box-like domain superfamily | IPR |
| F-box/LRR-repeat protein 15-like, leucin rich repeat domain | IPR |

**染色质调控潜力分析**: InterPro 注释了 5 个结构域条目。包含其他结构域类型。评分 7/10。

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
| 三维结构 | AlphaFold v6 | pLDDT 86.3 | — |
| 结构域 | InterPro | 5 个条目 | — |
| PPI | STRING | 0 partners | — |
| 定位 | HPA / UniProt | 待确认 | — |

**互证加分明细**:
- 进化保守性: 核候选保守蛋白 → +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3.0/5)

**核心优势**:
1. 较新颖，PubMed ≤100 篇
2. AlphaFold 结构质量好 (pLDDT>80)

**风险/不确定性**:
1. 结构可接受
2. '研究数据有限，需更多实验验证'

**下一步建议**:
- [ ] 在 TEreg 系统中检测 FBXL4 表达及定位
- [ ] 通过 co-IP/MS 验证 PPI 网络
- [ ] ChIP-seq 检查 FBXL4 在 TE 区域的 occupancy

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKA2
- Protein Atlas: https://www.proteinatlas.org/search/FBXL4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKA2
- STRING: https://string-db.org/network/9606.FBXL4
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q9UKA2/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[FBXL4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL4/FBXL4-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UKA2 |
| SMART | SM00367; |
| UniProt Domain [FT] | DOMAIN 277..332; /note="F-box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00080" |
| InterPro | IPR036047;IPR001810;IPR057207;IPR006553;IPR032675; |
| Pfam | PF25372;PF12937; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112234-FBXL4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SKP1 | Biogrid, Bioplex | true |
| BNIP3 | Biogrid | false |
| BNIP3L | Biogrid | false |
| CNPY2 | Bioplex | false |
| CUL1 | Biogrid | false |
| HSPA1A | Biogrid | false |
| MYO19 | Biogrid | false |
| RBX1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
