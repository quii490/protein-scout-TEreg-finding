---
type: protein-evaluation
gene: "TOE1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TOE1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TOE1 / hCaf1z|TOE-1 |
| 蛋白全称 | Target of EGR1 protein 1 |
| 蛋白大小 | 510 aa |
| UniProt ID | Q96GM8 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TOE1/IF_images/U2OS_1.jpg|U2OS]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TOE1/IF_images/NIH-3T3_1.jpg|NIH 3T3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | **24** | 细胞核+细胞质，UniProt 支持核定位 |
| 蛋白大小 | 10/10 | ×1 | **10** | 510 aa，处于理想范围 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 70 篇，中等研究热度 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 8 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **98.5/183** | **98.0/183** |  |  |  |
|  | **归一化总分** |  | **53.8/100** | **53.6/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, nucleolus, Nucleus speckle | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: 细胞核+细胞质，UniProt 支持核定位

#### 3.2 蛋白大小评估

**评价**: 510 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 70 |

**评价**: PubMed 70 篇，中等研究热度

**关键文献**:
1. Bai J et al. (2024). "The strigolactone receptor DWARF14 regulates flowering time in Arabidopsis". *Plant Cell*. PMID: 39235115
2. Zhang H et al. (2024). "A MYC-STAMBPL1-TOE1 positive feedback loop mediates EGFR stability in hepatocellular carcinoma". *Cell Rep*. PMID: 39388352
3. Zhu K et al. (2025). "Dynamic control of H2A.Zub and H3K27me3 by ambient temperature during cell fate determination in Arabidopsis". *Dev Cell*. PMID: 40267908
4. Huynh TN & Parker R (2023). "The PARN, TOE1, and USB1 RNA deadenylases and their roles in non-coding RNA regulation". *J Biol Chem*. PMID: 37544646
5. Ao JY et al. (2025). "Transcriptomic analysis reveals the potential role of TOE1 in hepatocellular carcinoma". *Sci Rep*. PMID: 41339427
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 510 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TOE1/TOE1-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | CAF1_poly(A)_ribonucleases |
| InterPro | RNase_CAF1 |
| InterPro | RNaseH-like_sf |
| InterPro | RNaseH_sf |
| InterPro | Znf_CCCH |
| Pfam | CAF1 |
| Pfam | zf-CCCH |
| PROSITE | ZF_C3H1 |

**染色质调控潜力分析**: 8 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| RPS3A | two hybrid pooling approach | 16169070 | — | — |
| SH3GL3 | two hybrid pooling approach | 16169070 | — | — |
| ABCF3 | two hybrid pooling approach | 16169070 | — | — |
| PNN | two hybrid pooling approach | 16169070 | — | — |
| AP2A1 | two hybrid pooling approach | 16169070 | — | — |
| CA12 | two hybrid pooling approach | 16169070 | — | — |
| RAB40C | two hybrid pooling approach | 16169070 | — | — |
| SQSTM1 | two hybrid pooling approach | 16169070 | — | — |
| UNC13B | two hybrid pooling approach | 16169070 | — | — |
| APLP1 | two hybrid pooling approach | 16169070 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

--

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 8 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 70 篇，中等研究热度
2. 核定位: 部分核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TOE1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132773-TOE1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TOE1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q96GM8
- STRING: https://string-db.org/network/9606.ENSG00000132773
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96GM8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TOE1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/TOE1/TOE1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000132773-TOE1/subcellular

![](https://images.proteinatlas.org/53775/2267_F12_112_blue_red_green.jpg)
![](https://images.proteinatlas.org/53775/2267_F12_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/53775/871_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/53775/871_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/53775/904_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/53775/904_E8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
