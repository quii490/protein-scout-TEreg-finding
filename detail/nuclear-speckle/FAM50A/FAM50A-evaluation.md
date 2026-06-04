---
type: protein-evaluation
gene: "FAM50A"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## FAM50A 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM50A |
| 蛋白大小 | 339 aa |
| UniProt ID | Q14320 (Protein FAM50A) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/FAM50A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/FAM50A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | x4 | 32 | HPA 标注: Nuclear speckles |
| 📏 蛋白大小 | 10/10 | x1 | 10 | 339 aa |
| 🆕 研究新颖性 | 10/10 | x5 | 50 | PubMed 17 篇 |
| 🏗️ 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT 75.9, v6 |
| 🧬 调控结构域 | 7/10 | x2 | 14 | InterPro 2 个结构域条目 |
| 🔗 PPI 网络 | 4/10 | x3 | 12 | STRING 0 partners |
| ➕ 互证加分 | — | max +3 | +0.5 | 核候选保守蛋白基线 |
| **原始总分** |  |  | **139.5/183** |  |
| **归一化总分** |  |  | **76.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA | Nuclear speckles | Tier1 |
| UniProt |  | — |

**结论**: HPA 标注: Nuclear speckles。核定位得分 8/10。

**IF 图片**: 暂无数据（HPA IF 图像已本地嵌入。


#### 3.2 蛋白大小评估
- 339 aa
- 大小适宜性评分：10/10

**评价**: 339 aa 蛋白，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 17 |
| 新颖性评分 | 10/10 |

**关键文献**:
1. Chen et al. (2025). "FAM50A drives breast cancer brain metastasis through interaction with C9ORF78 to enhance ʟ-asparagine production.". *Sci Adv*. PMID: 40531994
2. Thompson et al. (2021). "Combinatorial CRISPR screen identifies fitness effects of gene paralogues.". *Nat Commun*. PMID: 33637726
3. Hu et al. (2023). "Upregulation of FAM50A promotes cancer development.". *Med Oncol*. PMID: 37393403
4. Sun et al. (2025). "KSHV reprograms host RNA splicing via FAM50A to activate STAT3 and drive oncogenic cellular transformation.". *mBio*. PMID: 40503897
5. Lee et al. (2020). "Mutations in FAM50A suggest that Armfield XLID syndrome is a spliceosomopathy.". *Nat Commun*. PMID: 32703943
**评价**: PubMed 17 篇，属于极度新颖，几乎未被研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 75.9 |
| 有序区域 (pLDDT>70) 占比 | 69.7% |
| pLDDT>90 占比 | 26.3% |
| pLDDT 70-90 占比 | 43.4% |
| pLDDT 50-70 占比 | 17.7% |
| pLDDT<50 占比 | 12.7% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 查询中 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/FAM50A/FAM50A-PAE.png]]

**评价**: AlphaFold中等质量预测（pLDDT=75.9）。有高置信度折叠域，结构可信度高。评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| XAP5 protein | IPR |
| FAM50A/XAP5, C-terminal domain | IPR |

**染色质调控潜力分析**: InterPro 注释了 2 个结构域条目。包含其他结构域类型。评分 7/10。

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
| 三维结构 | AlphaFold v6 | pLDDT 75.9 | — |
| 结构域 | InterPro | 2 个条目 | — |
| PPI | STRING | 0 partners | — |
| 定位 | HPA / UniProt | Nuclear speckles | — |

**互证加分明细**:
- 进化保守性: 核候选保守蛋白 → +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (4.0/5)

**核心优势**:
1. 极度新颖，PubMed ≤20 篇
2. AlphaFold 结构中等

**风险/不确定性**:
1. 结构可接受
2. '研究数据有限，需更多实验验证'

**下一步建议**:
- [ ] 在 TEreg 系统中检测 FAM50A 表达及定位
- [ ] 通过 co-IP/MS 验证 PPI 网络
- [ ] ChIP-seq 检查 FAM50A 在 TE 区域的 occupancy

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14320
- Protein Atlas: https://www.proteinatlas.org/search/FAM50A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14320
- STRING: https://string-db.org/network/9606.FAM50A
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q14320/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[FAM50A-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/FAM50A/FAM50A-PAE.png]]


