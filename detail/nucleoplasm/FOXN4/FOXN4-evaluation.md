---
type: protein-evaluation
gene: "FOXN4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## FOXN4 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXN4 |
| 蛋白大小 | 517 aa |
| UniProt ID | Q96NZ1 (Forkhead box protein N4) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXN4/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXN4/IF_images/SH-SY5Y_1.jpg|SH-SY5Y]]


### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | x4 | 28 | 暂无数据（HPA IF 图像已本地嵌入。

| 📏 蛋白大小 | 10/10 | x1 | 10 | 517 aa |
| 🆕 研究新颖性 | 8/10 | x5 | 40 | PubMed 33 篇 |
| 🏗️ 三维结构 | 6/10 | x3 | 18 | AlphaFold pLDDT 57.1, v6 |
| 🧬 调控结构域 | 10/10 | x2 | 20 | InterPro 5 个结构域条目 |
| 🔗 PPI 网络 | 6/10 | x3 | 18 | STRING 30 partners |
| ➕ 互证加分 | — | max +3 | +0.5 | 核候选保守蛋白基线 |
| **原始总分** |  |  | **134.5/183** |  |
| **归一化总分** |  |  | **73.5/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA | 暂无数据 | Tier1 |
| UniProt |  | — |

**结论**: 暂无数据（HPA IF 图像已本地嵌入。


#### 3.2 蛋白大小评估
- 517 aa
- 大小适宜性评分：10/10

**评价**: 517 aa 蛋白，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 33 |
| 新颖性评分 | 8/10 |

**评价**: PubMed 33 篇，属于非常新颖，少数基础研究。

**关键文献**:
1. Nusser A et al. (2025). "Developmental trajectory and evolutionary origin of thymic mimetic cells". *Nature*. PMID: 40500437
2. Katoh M & Katoh M (2004). "Human FOX gene family (Review)". *Int J Oncol*. PMID: 15492844
3. Morimoto R et al. (2021). "Evolution of thymopoietic microenvironments". *Open Biol*. PMID: 33622100
4. Xiang M & Li S (2013). "Foxn4: a multi-faceted transcriptional regulator of cell fates in vertebrate development". *Sci China Life Sci*. PMID: 24008385
5. Wang J et al. (2023). "FOXN4 affects myocardial ischemia-reperfusion injury through HIF-1α/MMP2-mediated ferroptosis of cardiomyocytes". *Cell Mol Biol (Noisy-le-grand)*. PMID: 37605566
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 57.1 |
| 有序区域 (pLDDT>70) 占比 | 21.5% |
| pLDDT>90 占比 | 20.5% |
| pLDDT 70-90 占比 | 1.0% |
| pLDDT 50-70 占比 | 20.1% |
| pLDDT<50 占比 | 58.4% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 查询中 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXN4/FOXN4-PAE.png]]

**评价**: AlphaFold预测质量偏低（pLDDT=57.1）。大量无序区域。评分 6/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| Fork head domain | IPR |
| Fork head domain conserved site 2 | IPR |
| Winged helix-like DNA-binding domain superfamily | IPR |
| Winged helix DNA-binding domain superfamily | IPR |
| Forkhead box protein N2/3-like | IPR |

**染色质调控潜力分析**: InterPro 注释了 5 个结构域条目。包含 forkhead/winged-helix DNA 结合域，为典型转录因子。评分 10/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| NEUROD4 | 0.944 | — | — |
| NEUROD1 | 0.868 | — | — |
| PROX1 | 0.808 | — | — |
| PTF1A | 0.754 | — | — |
| ATOH7 | 0.699 | — | — |
| VSX2 | 0.688 | — | — |
| VSX1 | 0.685 | — | — |
| BARHL2 | 0.669 | — | — |
| ZNF862 | 0.617 | — | — |
| POU4F2 | 0.600 | — | — |

**GO-CC 复合体**: 从 UniProt GO 注释提取

**PPI 互证分析**:
- STRING 高置信度 (>0.7) partners: 4 个
- 调控相关比例: 待进一步分析

**评价**: STRING 数据库显示 30 个互作伙伴。评分 6/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT 57.1 | — |
| 结构域 | InterPro | 5 个条目 | — |
| PPI | STRING | 30 partners | — |
| 定位 | HPA / UniProt | 待确认 | — |

**互证加分明细**:
- 进化保守性: 核候选保守蛋白 → +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (4.0/5)

**核心优势**:
1. 较新颖，PubMed ≤100 篇
2. 核蛋白候选

**风险/不确定性**:
1. AlphaFold 预测质量偏低，大量无序区域
2. '研究数据有限，需更多实验验证'

**下一步建议**:
- [ ] 在 TEreg 系统中检测 FOXN4 表达及定位
- [ ] 通过 co-IP/MS 验证 PPI 网络
- [ ] ChIP-seq 检查 FOXN4 在 TE 区域的 occupancy

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96NZ1
- Protein Atlas: https://www.proteinatlas.org/search/FOXN4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96NZ1
- STRING: https://string-db.org/network/9606.FOXN4
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q96NZ1/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[FOXN4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXN4/FOXN4-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96NZ1 |
| SMART | SM00339; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001766;IPR047119;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00250; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000139445-FOXN4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATXN1 | Intact | false |
| FHL3 | Intact | false |
| RFX2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
