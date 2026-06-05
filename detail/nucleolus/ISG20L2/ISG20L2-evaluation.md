---
type: protein-evaluation
gene: "ISG20L2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ISG20L2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ISG20L2 / ISG20L2|HSD38|REXO2L|bA255A11.4 |
| 蛋白全称 | Interferon-stimulated 20 kDa exonuclease-like 2 |
| 蛋白大小 | 353 aa / ~38.8 kDa |
| UniProt ID |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ISG20L2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ISG20L2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | 严格核蛋白：UniProt Nucleus + GO 支持（HPA 无 IF 数据） |
| 蛋白大小 | 10/10 | x1 | 10 | 353 aa，适宜 |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed 12 篇 |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT 65-80，或部分 PDB |
| 调控结构域 | 8/10 | x2 | 16 | nucleic acid binding 相关域，多库确认 (8/10) |
| PPI 网络 | 2/10 | x3 | 6 | 互作数据有限 (2/10) |
| 互证加分 | +0 | max +3 | +0 | — |
| **原始总分** |  |  | **139/183** |  |
| **归一化总分** |  |  | **76.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleus, nucleolus | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus, nucleolus | — |
| GO Cellular Component | nucleolus | nucleus | — |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

#### 3.2 蛋白大小评估

**评价**: 353 aa (~38.8 kDa)，适合常规生化实验和结构解析，大小接近理想范围（200–800 aa）。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 12 |
| 新颖性评级 | 极度新颖 |

**主要研究方向**:
- Interferon-stimulated 20 kDa exonuclease-like 2 的功能研究
- 转录调控/信号传导相关

**关键文献**:
1. Rodríguez-Galán et al. (2023). "ISG20L2: an RNA nuclease regulating T cell activation.". *Cell Mol Life Sci*. PMID: 37646974
2. Ma et al. (2024). "Molecular mechanism of human ISG20L2 for the ITS1 cleavage in the processing of 18S precursor ribosomal RNA.". *Nucleic Acids Res*. PMID: 38153123
3. Yang et al. (2022). "ISG20L2 suppresses bortezomib antimyeloma activity by attenuating bortezomib binding to PSMB5.". *JCI Insight*. PMID: 36040812
4. Zhu et al. (2019). "High miR-139-3p expression predicts a better prognosis for hepatocellular carcinoma: a pooled analysis.". *J Int Med Res*. PMID: 30394818
5. Qin et al. (2021). "Immunogenomic Landscape Analysis of Prognostic Immune-Related Genes in Hepatocellular Carcinoma.". *J Healthc Eng*. PMID: 34745496
**评价**: PubMed 12 篇，几乎未被研究，属于极度新颖的蛋白。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 全局 pLDDT | 72.81 |
| pLDDT > 90 占比 | 50% |
| pLDDT > 70 占比 | 56% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 1 个：7YW5 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ISG20L2/ISG20L2-PAE.png]]

**评价**: AlphaFold pLDDT 65-80，或部分 PDB。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt InterPro | ISG20_DEDDh, REXO1/3/4-like, Ribonucl_H, RNaseH-like_sf, RNaseH_sf |
| Pfam | RNase_T |

**染色质调控潜力分析**: 未注释到经典染色质/DNA 结合结构域，但属于新颖蛋白（基线不扣分）。AlphaFold 预测有可辨识折叠域，存在新结构域发现潜力。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| PCNA | 0.416 | — | — |
| NOL9 | 0.000 | — | — |
| NPM1 | 0.190 | — | — |
| EML1 | 0.600 | — | — |
| WDR18 | 0.045 | — | — |


**已知复合体成员** (GO Cellular Component):
- 未注释到特定染色质调控复合体

**PPI 互证分析**:
- 物理互作证据：IntAct 有实验互作数据
- STRING 预测：30 个 partner，>0.7 高置信度较少
- 调控相关比例：需进一步验证

**评价**: 互作数据有限 (2/10)。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=72.81, PDB=1个 | — |
| 结构域 | InterPro / Pfam / SMART | ISG20_DEDDh, REXO1/3/4-like, Ribonucl_H, RNaseH-like_sf, RNaseH_sf | — |
| PPI | STRING + IntAct | 有网络 | — |
| 定位 | UniProt / GO | Nucleus, nucleolus | — |

**互证加分明细**: 无额外互证加分。

### 4. 总体评价

**推荐等级**: ★★★☆☆ (76.0/100)

**核心优势**:
1. 极度新颖（PubMed 12 篇），niche 空间充足
2. 严格核蛋白：UniProt Nucleus + GO 支持（HPA 无 IF 数据）
3. AlphaFold pLDDT 65-80，或部分 PDB

**风险/不确定性**:
1. HPA IF 数据缺失，核定位待实验验证
2. PPI 数据有限，调控网络待探索
3. 功能研究较少，生物学角色待阐明

**下一步建议**:
- [ ] 获取 HPA IF 数据或多重 IF 验证核定位
- [ ] Co-IP/MS 鉴定互作伙伴
- [ ] ChIP-seq 分析基因组结合位点（如为 TF/染色质蛋白）

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ISG20L2
- STRING: https://string-db.org/network/9606.ENSP00000000
- IntAct: https://www.ebi.ac.uk/intact/search?query=ISG20L2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ISG20L2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/ISG20L2/ISG20L2-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000143319-ISG20L2/subcellular

![](https://images.proteinatlas.org/54285/834_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/54285/834_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/54285/856_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/54285/856_E1_3_red_green.jpg)
![](https://images.proteinatlas.org/54285/877_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/54285/877_H7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
