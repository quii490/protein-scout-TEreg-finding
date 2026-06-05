---
type: protein-evaluation
gene: "ILF2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ILF2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ILF2 / ILF2|NF45|PRO3063 |
| 蛋白全称 | Interleukin enhancer-binding factor 2 |
| 蛋白大小 | 390 aa / ~42.9 kDa |
| UniProt ID |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ILF2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ILF2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | 严格核蛋白：UniProt Nucleus + GO 支持（HPA 无 IF 数据） |
| 蛋白大小 | 10/10 | x1 | 10 | 390 aa，适宜 |
| 研究新颖性 | 2/10 | x5 | 30 | PubMed 96 篇 |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold pLDDT≥80，高质量预测 |
| 调控结构域 | 8/10 | x2 | 16 | nucleic acid binding 相关域，多库确认 (8/10) |
| PPI 网络 | 4/10 | x3 | 12 | STRING 预测互作，调控因子部分 (4/10) |
| 互证加分 | +1 | max +3 | +1 | — |
|  | **原始总分** |  | **109/183** | **108.0/183** |  |  |
|  | **归一化总分** |  | **59.6/100** | **59.0/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleus, nucleolus | Cytoplasm | Nucleus | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus, nucleolus | Cytoplasm | Nucleus | — |
| GO Cellular Component | cytosol | extracellular region | ficolin-1-rich granule lumen | membrane | nucleolus | nucleoplasm | — |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

#### 3.2 蛋白大小评估

**评价**: 390 aa (~42.9 kDa)，适合常规生化实验和结构解析，大小接近理想范围（200–800 aa）。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 96 |
| 新颖性评级 | 有一定研究但 niche 空间充足 |

**主要研究方向**:
- Interleukin enhancer-binding factor 2 的功能研究
- 转录调控/信号传导相关

**关键文献**:
1. Surka et al. (2021). "CC-90009, a novel cereblon E3 ligase modulator, targets acute myeloid leukemia blasts and leukemia stem cells.". *Blood*. PMID: 33197925
2. Li et al. (2024). "The lncRNA SNHG26 drives the inflammatory-to-proliferative state transition of keratinocyte progenitor cells during wound healing.". *Nat Commun*. PMID: 39366968
3. Sun et al. (2024). "ILF2: a multifaceted regulator in malignant tumors and its prospects as a biomarker and therapeutic target.". *Front Oncol*. PMID: 39735599
4. Zhang et al. (2024). "AP3B1 facilitates PDIA3/ERP57 function to regulate rabies virus glycoprotein selective degradation and viral entry.". *Autophagy*. PMID: 39128851
5. Xie et al. (2024). "Single-cell RNA sequencing elucidated the landscape of breast cancer brain metastases and identified ILF2 as a potential therapeutic target.". *Cell Prolif*. PMID: 38943472
**评价**: PubMed 96 篇，有一定研究基础，但 niche 空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 全局 pLDDT | 89.62 |
| pLDDT > 90 占比 | 85% |
| pLDDT > 70 占比 | 87% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 0 个 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ILF2/ILF2-PAE.png]]

**评价**: AlphaFold pLDDT≥80，高质量预测。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt InterPro | DZF_dom, DZF_dom_C, DZF_dom_N, ILF2, NT_sf |
| Pfam | DZF_C, DZF_N |

**染色质调控潜力分析**: 未注释到经典染色质/DNA 结合结构域，但属于新颖蛋白（基线不扣分）。AlphaFold 预测有可辨识折叠域，存在新结构域发现潜力。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ILF3 | 0.922 | — | — |
| HNRNPC | 0.599 | — | — |
| DHX9 | 0.621 | — | — |
| HNRNPM | 0.000 | — | — |
| HNRNPH1 | 0.362 | — | — |


**已知复合体成员** (GO Cellular Component):
- ribonucleoprotein complex

**PPI 互证分析**:
- 物理互作证据：IntAct 有实验互作数据
- STRING 预测：30 个 partner，>0.7 高置信度较少
- 调控相关比例：需进一步验证

**评价**: STRING 预测互作，调控因子部分 (4/10)。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=89.62, PDB=0个 | — |
| 结构域 | InterPro / Pfam / SMART | DZF_dom, DZF_dom_C, DZF_dom_N, ILF2, NT_sf | — |
| PPI | STRING + IntAct | 有网络 | — |
| 定位 | UniProt / GO | Nucleus, nucleolus | Cytoplasm | Nucleus | — |

**互证加分明细**: STRONG + UniProt/GO 一致，+1。

### 4. 总体评价

**推荐等级**: ★★★☆☆ (70.5/100)

**核心优势**:
1. 研究新颖（PubMed 96 篇）
2. 严格核蛋白：UniProt Nucleus + GO 支持（HPA 无 IF 数据）
3. AlphaFold pLDDT≥80，高质量预测

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
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ILF2
- STRING: https://string-db.org/network/9606.ENSP00000000
- IntAct: https://www.ebi.ac.uk/intact/search?query=ILF2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ILF2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/ILF2/ILF2-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000143621-ILF2/subcellular

![](https://images.proteinatlas.org/72048/1975_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/72048/1975_D3_4_red_green.jpg)
![](https://images.proteinatlas.org/72048/2055_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/72048/2055_H10_4_red_green.jpg)
![](https://images.proteinatlas.org/72048/2162_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/72048/2162_D6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
