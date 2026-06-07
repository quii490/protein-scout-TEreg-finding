---
type: protein-evaluation
gene: "FUBP3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## FUBP3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FUBP3 |
| 蛋白大小 | 572 aa |
| UniProt ID | Q96I24 (Far upstream element-binding protein 3) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FUBP3/IF_images/NIH-3T3_1.jpg|NIH 3T3]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FUBP3/IF_images/U2OS_1.jpg|U2OS]]


### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | x4 | 32 | HPA 标注: Nucleoplasm |
| 📏 蛋白大小 | 10/10 | x1 | 10 | 572 aa |
| 🆕 研究新颖性 | 8/10 | x5 | 40 | PubMed 21 篇 |
| 🏗️ 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT 65.8, v6 |
| 🧬 调控结构域 | 7/10 | x2 | 14 | InterPro 3 个结构域条目 |
| 🔗 PPI 网络 | 8/10 | x3 | 24 | STRING 30 partners |
| ➕ 互证加分 | — | max +3 | +0.5 | 核候选保守蛋白基线 |
| **原始总分** |  |  | **141.5/183** |  |
| **归一化总分** |  |  | **77.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA | Nucleoplasm | Tier1 |
| UniProt |  | — |

**结论**: HPA 标注: Nucleoplasm。核定位得分 8/10。

**IF 图片**: 暂无数据（HPA IF 图像已本地嵌入。


#### 3.2 蛋白大小评估
- 572 aa
- 大小适宜性评分：10/10

**评价**: 572 aa 蛋白，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 21 |
| 新颖性评分 | 8/10 |

**评价**: PubMed 21 篇，属于非常新颖，少数基础研究。

**关键文献**:
1. Zhai X et al. (2023). "N protein of PEDV plays chess game with host proteins by selective autophagy". *Autophagy*. PMID: 36861818
2. Cenik BK et al. (2024). "TurboCas: A method for locus-specific labeling of genomic regions and isolating their associated protein interactome". *Mol Cell*. PMID: 39706164
3. Wu Z et al. (2025). "LncRNA TMEM99 Complexes with IGF2BP2 to Inhibit Autophagy in Lung Adenocarcinoma". *Adv Sci (Weinh)*. PMID: 40704413
4. Chen T et al. (2025). "Stem loop binding protein promotes SARS-CoV-2 replication via -1 programmed ribosomal frameshifting". *Signal Transduct Target Ther*. PMID: 40514371
5. Tu R et al. (2024). "USP7 depletion potentiates HIF2α degradation and inhibits clear cell renal cell carcinoma progression". *Cell Death Dis*. PMID: 39406703
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 65.8 |
| 有序区域 (pLDDT>70) 占比 | 47.7% |
| pLDDT>90 占比 | 22.0% |
| pLDDT 70-90 占比 | 25.7% |
| pLDDT 50-70 占比 | 15.0% |
| pLDDT<50 占比 | 37.2% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 查询中 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FUBP3/FUBP3-PAE.png]]

**评价**: AlphaFold中等质量预测（pLDDT=65.8）。部分区域有序。评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| K Homology domain | IPR |
| K Homology domain, type 1 | IPR |
| K Homology domain, type 1 superfamily | IPR |

**染色质调控潜力分析**: InterPro 注释了 3 个结构域条目。包含其他结构域类型。评分 7/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| FBP1 | 0.889 | — | — |
| HNRNPF | 0.844 | — | — |
| QKI | 0.843 | — | — |
| PUF60 | 0.813 | — | — |
| FUBP1 | 0.756 | — | — |
| MATR3 | 0.684 | — | — |
| MATR3-2 | 0.611 | — | — |
| HNRNPM | 0.597 | — | — |
| PCBP2 | 0.584 | — | — |
| MYC | 0.584 | — | — |

**GO-CC 复合体**: 从 UniProt GO 注释提取

**PPI 互证分析**:
- STRING 高置信度 (>0.7) partners: 5 个
- 调控相关比例: 待进一步分析

**评价**: STRING 数据库显示 30 个互作伙伴。评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT 65.8 | — |
| 结构域 | InterPro | 3 个条目 | — |
| PPI | STRING | 30 partners | — |
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
- [ ] 在 TEreg 系统中检测 FUBP3 表达及定位
- [ ] 通过 co-IP/MS 验证 PPI 网络
- [ ] ChIP-seq 检查 FUBP3 在 TE 区域的 occupancy

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96I24
- Protein Atlas: https://www.proteinatlas.org/search/FUBP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96I24
- STRING: https://string-db.org/network/9606.FUBP3
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q96I24/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[FUBP3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FUBP3/FUBP3-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96I24 |
| SMART | SM00322; |
| UniProt Domain [FT] | DOMAIN 77..141; /note="KH 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00117"; DOMAIN 162..228; /note="KH 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00117"; DOMAIN 253..317; /note="KH 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00117"; DOMAIN 354..421; /note="KH 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00117" |
| InterPro | IPR004087;IPR004088;IPR036612; |
| Pfam | PF00013; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000107164-FUBP3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PAX9 | Intact, Biogrid | true |
| QKI | Intact, Biogrid | true |
| ACE2 | Biogrid | false |
| AKAP1 | Biogrid | false |
| CALCOCO2 | Biogrid | false |
| CAPZB | Opencell | false |
| DAZAP1 | Biogrid | false |
| FBL | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
