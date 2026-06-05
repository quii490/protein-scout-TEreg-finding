---
type: protein-evaluation
gene: "JADE1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## JADE1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | JADE1 / JADE1|PHF17|KIAA1807 |
| 蛋白全称 | Protein Jade-1 |
| 蛋白大小 | 842 aa / ~92.6 kDa |
| UniProt ID |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/JADE1/IF_images/HeLa_1.jpg|HeLa]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/JADE1/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | 核定位：UniProt Nucleus + 微量胞质背景 |
| 蛋白大小 | 8/10 | x1 | 8 | 842 aa，适宜 |
| 研究新颖性 | 6/10 | x5 | 40 | PubMed 48 篇 |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT 65-80，或部分 PDB |
| 调控结构域 | 10/10 | x2 | 20 | 明确 chromatin/DNA-binding 结构域 |
| PPI 网络 | 4/10 | x3 | 12 | STRING 预测互作，调控因子部分 (4/10) |
| 互证加分 | +1 | max +3 | +1 | — |
|  | **原始总分** |  | **124/183** | **123.0/183** |  |  |
|  | **归一化总分** |  | **67.8/100** | **67.2/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleus | Chromosome | Cytoplasm | Cytoplasm, cytoskeleton, cilium basal body | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus | Chromosome | Cytoplasm | Cytoplasm, cytoskeleton, cilium basal body | — |
| GO Cellular Component | centrosome | ciliary basal body | cytoplasm | cytosol | histone acetyltransferase complex | nuclear speck | — |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

#### 3.2 蛋白大小评估

**评价**: 842 aa (~92.6 kDa)，大小偏大，可能增加实验难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 48 |
| 新颖性评级 | 非常新颖 |

**主要研究方向**:
- Protein Jade-1 的功能研究
- 转录调控/信号传导相关

**关键文献**:
1. Niu et al. (2024). "HBO1 catalyzes lysine lactylation and mediates histone H3K9la to regulate gene transcription.". *Nat Commun*. PMID: 38670996
2. Su et al. (2024). "Multifunctional acyltransferase HBO1: a key regulatory factor for cellular functions.". *Cell Mol Biol Lett*. PMID: 39543485
3. Zhu et al. (2025). "JADE1 is not essential for spermatogenesis and male fertility in mice.". *Mol Biol Rep*. PMID: 41379394
4. Wang et al. (2024). "JADE1 is dispensable for the brain development in mice.". *Biochem Biophys Res Commun*. PMID: 38171233
5. Panchenko et al. (2016). "Structure, function and regulation of jade family PHD finger 1 (JADE1).". *Gene*. PMID: 27155521
**评价**: PubMed 48 篇，研究较少，属于非常新颖的蛋白。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 全局 pLDDT | 61.66 |
| pLDDT > 90 占比 | 25% |
| pLDDT > 70 占比 | 46% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 2 个：8GDX, 8GE0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/JADE1/JADE1-PAE.png]]

**评价**: AlphaFold pLDDT 65-80，或部分 PDB。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt InterPro | Enhancer_polycomb-like_N, EPHD, Histone_Mod_Regulator, Jade-1_PHD, Zinc_finger_PHD-type_CS, Znf_FYVE_PHD, Znf_PHD, Znf_PHD-finger |
| Pfam | EPL1, PHD_2, zf-HC5HC2H_2 |

**染色质调控潜力分析**: 包含明确的 DNA 结合/染色质调控结构域：EPHD, Histone_Mod_Regulator, Jade-1_PHD, Zinc_finger_PHD-type_CS, Znf_FYVE_PHD, Znf_PHD, Znf_PHD-finger

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| KAT7 | 0.892 | — | — |
| ING4 | 0.767 | — | — |
| MEAF6 | 0.836 | — | — |
| ING5 | 0.801 | — | — |
| VHL | 0.708 | — | — |


**已知复合体成员** (GO Cellular Component):
- ciliary basal body | histone acetyltransferase complex | nuclear speck

**PPI 互证分析**:
- 物理互作证据：IntAct 有实验互作数据
- STRING 预测：30 个 partner，>0.7 高置信度有
- 调控相关比例：需进一步验证

**评价**: STRING 预测互作，调控因子部分 (4/10)。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=61.66, PDB=2个 | — |
| 结构域 | InterPro / Pfam / SMART | Enhancer_polycomb-like_N, EPHD, Histone_Mod_Regulator, Jade-1_PHD, Zinc_finger_P | — |
| PPI | STRING + IntAct | 有网络 | — |
| 定位 | UniProt / GO | Nucleus | Chromosome | Cytoplasm | Cytoplasm, cytoskeleton, cilium basal body | — |

**互证加分明细**: STRONG + UniProt/GO 一致，+1。

### 4. 总体评价

**推荐等级**: ★★★☆☆ (73.2/100)

**核心优势**:
1. 研究新颖（PubMed 48 篇）
2. 核定位：UniProt Nucleus + 微量胞质背景
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
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=JADE1
- STRING: https://string-db.org/network/9606.ENSP00000000
- IntAct: https://www.ebi.ac.uk/intact/search?query=JADE1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[JADE1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/JADE1/JADE1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000077684-JADE1/subcellular

![](https://images.proteinatlas.org/72897/2176_D12_69_blue_red_green.jpg)
![](https://images.proteinatlas.org/72897/2176_D12_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/72897/1950_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/72897/1950_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/72897/1968_G8_3_red_green.jpg)
![](https://images.proteinatlas.org/72897/1968_G8_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
