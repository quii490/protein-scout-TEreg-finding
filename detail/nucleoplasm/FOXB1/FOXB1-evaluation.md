---
type: protein-evaluation
gene: "FOXB1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## FOXB1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXB1 |
| 蛋白大小 | 325 aa |
| UniProt ID | Q99853 (Forkhead box protein B1) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXB1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXB1/IF_images/HEK293_1.jpg|HEK293]]


### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | x4 | 28 | 暂无数据（HPA IF 图像已本地嵌入。

| 📏 蛋白大小 | 10/10 | x1 | 10 | 325 aa |
| 🆕 研究新颖性 | 10/10 | x5 | 50 | PubMed 18 篇 |
| 🏗️ 三维结构 | 6/10 | x3 | 18 | AlphaFold pLDDT 64.9, v6 |
| 🧬 调控结构域 | 10/10 | x2 | 20 | InterPro 7 个结构域条目 |
| 🔗 PPI 网络 | 2/10 | x3 | 6 | STRING 16 partners |
| ➕ 互证加分 | — | max +3 | +0.5 | 核候选保守蛋白基线 |
| **原始总分** |  |  | **132.5/183** |  |
| **归一化总分** |  |  | **72.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA | 暂无数据 | Tier1 |
| UniProt |  | — |

**结论**: 暂无数据（HPA IF 图像已本地嵌入。


#### 3.2 蛋白大小评估
- 325 aa
- 大小适宜性评分：10/10

**评价**: 325 aa 蛋白，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 18 |
| 新颖性评分 | 10/10 |

**评价**: PubMed 18 篇，属于极度新颖，几乎未被研究。

**关键文献**:
1. Katoh M & Katoh M (2004). "Human FOX gene family (Review)". *Int J Oncol*. PMID: 15492844
2. Bilella A et al. (2016). "The Foxb1-expressing neurons of the ventrolateral hypothalamic parvafox nucleus project to defensive circuits". *J Comp Neurol*. PMID: 27292133
3. Zhang Y et al. (2017). "Foxb1 Regulates Negatively the Proliferation of Oligodendrocyte Progenitors". *Front Neuroanat*. PMID: 28725186
4. Bilella A et al. (2016). "Birthdate of parvalbumin-neurons in the Parvafox-nucleus of the lateral hypothalamus". *Brain Res*. PMID: 26764531
5. Zhao T et al. (2007). "Foxb1-driven Cre expression in somites and the neuroepithelium of diencephalon, brainstem, and spinal cord". *Genesis*. PMID: 18064677
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 64.9 |
| 有序区域 (pLDDT>70) 占比 | 38.4% |
| pLDDT>90 占比 | 21.2% |
| pLDDT 70-90 占比 | 17.2% |
| pLDDT 50-70 占比 | 28.9% |
| pLDDT<50 占比 | 32.6% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 查询中 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXB1/FOXB1-PAE.png]]

**评价**: AlphaFold预测质量偏低（pLDDT=64.9）。部分区域有序。评分 6/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| Fork head domain | IPR |
| Fork head domain conserved site1 | IPR |
| Fork head domain conserved site 2 | IPR |
| Winged helix-like DNA-binding domain superfamily | IPR |
| Winged helix DNA-binding domain superfamily | IPR |
| Forkhead box protein B1/B2, forkhead domain | IPR |
| Forkhead box domain-containing protein | IPR |

**染色质调控潜力分析**: InterPro 注释了 7 个结构域条目。包含 forkhead/winged-helix DNA 结合域，为典型转录因子。评分 10/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| FOXC2 | 0.555 | — | — |
| OTP | 0.515 | — | — |
| LHX5 | 0.510 | — | — |
| EVX1 | 0.484 | — | — |
| LHX1 | 0.471 | — | — |
| NEUROG1 | 0.458 | — | — |
| TOMM40 | 0.458 | — | — |
| SOX5 | 0.441 | — | — |
| NEUROG3 | 0.437 | — | — |
| IRX1 | 0.431 | — | — |

**GO-CC 复合体**: 从 UniProt GO 注释提取

**PPI 互证分析**:
- STRING 高置信度 (>0.7) partners: 0 个
- 调控相关比例: 待进一步分析

**评价**: STRING 数据库显示 16 个互作伙伴。评分 2/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT 64.9 | — |
| 结构域 | InterPro | 7 个条目 | — |
| PPI | STRING | 16 partners | — |
| 定位 | HPA / UniProt | 待确认 | — |

**互证加分明细**:
- 进化保守性: 核候选保守蛋白 → +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (4.0/5)

**核心优势**:
1. 极度新颖，PubMed ≤20 篇
2. 核蛋白候选

**风险/不确定性**:
1. 结构质量中等
2. '研究数据有限，需更多实验验证'

**下一步建议**:
- [ ] 在 TEreg 系统中检测 FOXB1 表达及定位
- [ ] 通过 co-IP/MS 验证 PPI 网络
- [ ] ChIP-seq 检查 FOXB1 在 TE 区域的 occupancy

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99853
- Protein Atlas: https://www.proteinatlas.org/search/FOXB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99853
- STRING: https://string-db.org/network/9606.FOXB1
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q99853/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[FOXB1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXB1/FOXB1-PAE.png]]


