---
type: protein-evaluation
gene: "AHCYL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AHCYL2 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AHCYL2 / KIAA0828 |
| 蛋白大小 | 611 aa / 66.7 kDa |
| UniProt ID | Q96HN2 |
| 蛋白全名 | Adenosylhomocysteinase 3 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Cytosol |
| HPA IF 附加定位 | Nucleoplasm, Vesicles |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA主定位Cytosol，Nucleoplasm为附加；UniProt注释Cytoplasm；核定位不主导 |
| 蛋白大小 | 10/10 | ×1 | 10 | 611aa/66.7kDa，理想实验范围 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | pLDDT=79.2；PDB 3GVP (X-ray 2.25A) |
| 调控结构域 | 8/10 | ×2 | 16 | IPR000043 AdoHcyase + IPR015878 NAD binding + IPR036291 NAD(P)超家族；经典代谢酶折叠 |
| PPI网络 | 7/10 | ×3 | 21 | AHCYL1(0.964实验), CBS(0.975), BHMT(0.975)；IntAct 15条含TRAF6/BAP1/CSNK1E |
| **加权总分** | | | **137/180**** | |
| **归一化总分 (÷1.83)** | | | **74.9/100**** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Cytosol (main), Nucleoplasm (additional), Vesicles (additional) | Approved |
| UniProt | Cytoplasm (by similarity), Microsome (by similarity) | |
| GO-CC | GO:0005829 (cytosol, IBA), GO:0043005 (neuron projection, IEA) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。HPA Approved 级别 IF 明确将 Cytosol 列为主定位，Nucleoplasm 为附加定位。蛋白主要在胞质中发挥功能，但有一定核分布。**评分: 4/10**。

#### 3.2 蛋白大小评估

611 aa / 66.7 kDa。大小处于 200-800 aa 理想实验范围，足够包含完整酶活结构域，又不过大难以重组表达。**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 19 |
| PubMed symbol_only | 29 |
| 别名 | KIAA0828 |
| 主要方向 | 钠/碳酸氢盐共转运体调控、IRBIT家族信号、视网膜发育 |

**评价**: PubMed 仅 19 篇 (strict)，极度新颖。AHCYL2 属于 IRBIT 家族，调控 NBCe1-B 钠/碳酸氢盐共转运体活性。研究主要来自韩国团队。**评分: 10/10** (≤20篇)。

**关键文献**:
1. Park PW et al. (2016). "Ahcyl2 upregulates NBCe1-B via multiple serine residues of the PEST domain-mediated association." *Korean J Physiol Pharmacol*. PMID: 27382360 — 核心功能文献
2. Campbell WA et al. (2023). "Chromatin access regulates the formation of Müller glia-derived progenitor cells in the retina." *Glia*. PMID: 36971459 — 染色质可及性与AHCYL2
3. Liu Y et al. (2025). "IRBITs, signaling molecules of great functional diversity." *Pflugers Arch*. PMID: 40445299 — IRBIT家族综述
4. Praus F et al. (2023). "Panomics reveals patient individuality as the major driver of colorectal cancer progression." *J Transl Med*. PMID: 36691026
5. Yang C et al. (2023). "The identification of metabolism-related subtypes and potential treatments for idiopathic pulmonary fibrosis." *Front Pharmacol*. PMID: 37274115

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 79.2 |
| pLDDT > 90 (Very High) | 66.8% |
| pLDDT 70-90 (High) | 5.6% |
| pLDDT 50-70 (Medium) | 1.1% |
| pLDDT < 50 (Low) | 26.5% |
| 有序区域 (pLDDT>70) | 72.4% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 3GVP (X-ray, 2.25A, chains A/B/C/D=175-607) |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。PDB 3GVP 为截短体 X-ray 晶体结构 (2.25 A)，涵盖 175-607 位残基（约占全长 70%），提供可靠实验结构信息。AlphaFold pLDDT 79.2，26.5% 无序区域可能位于 N 端。**评分: 8/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR000043 (Adenosylhomocysteinase); IPR015878 (S-adenosyl-L-homocysteine hydrolase, NAD binding domain); IPR036291 (NAD(P)-binding domain superfamily); IPR042172 (Adenosylhomocysteinase, eukaryotic/archaeal); IPR020082 (S-adenosyl-L-homocysteine hydrolase, conserved site) |
| Pfam | PF00670 (S-adenosyl-L-homocysteine hydrolase, NAD binding domain); PF05221 (Adenosylhomocysteinase) |

AHCYL2 为 S-腺苷同型半胱氨酸水解酶家族成员 (AHCY-like 2)，含经典的双结构域折叠 (NAD binding + catalytic domain)。虽为代谢酶，AHCYL2 与同家族 AHCYL1 (IRBIT) 一样具有非酶信号功能——通过 PEST 结构域介导 NBCe1-B 调控。NAD 结合域与代谢和信号双重功能相关。**评分: 8/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验证据 | 功能类别 |
|---------|-------|---------|---------|
| BHMT | 0.975 | 0 | 同型半胱氨酸代谢 |
| CBS | 0.975 | 0.07 | 转硫途径 |
| BHMT2 | 0.973 | 0 | 甜菜碱-同型半胱氨酸甲基转移酶 |
| MTR | 0.972 | 0 | 甲硫氨酸合成酶 |
| CTH | 0.971 | 0.069 | 半胱氨酸代谢 |
| AHCYL1 | 0.964 | 0.651 | IRBIT家族，实验互作强 |
| AHCY | 0.921 | 0.208 | 经典AdoHcyase，实验互作 |
| KYAT1 | 0.920 | 0 | 犬尿氨酸转氨酶 |
| DNMT1 | 0.919 | 0 | DNA甲基转移酶 |
| DNMT3B | 0.913 | 0 | DNA甲基转移酶 |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF6 | anti bait co-IP | 17353931 |
| CSNK1E | TAP | 23455922 |
| CLK4 | TAP | 23602568 |
| BAP1 | anti tag co-IP | 19615732 |
| SLX4 | anti tag co-IP | 19596235 |
| FAM13A | anti tag co-IP | 32203420 |
| EZR | BioID | 29568061 |
| TGOLN2 | BioID | 29568061 |

**PPI 互证分析**:
- AHCYL1 实验互作 (0.651) 为最可靠伙伴，同属 IRBIT 信号家族
- DNMT1/DNMT3B 的文本挖掘关联暗示潜在的表观遗传调控连接
- TRAF6 和 CSNK1E 互作连接至 NF-kB 和 Wnt 信号通路
- AHCY 代谢酶互作指向 S-腺苷甲硫氨酸循环与甲基化代谢的交叉

**评分: 7/10** (IRBIT家族互作 + DNMT关联 + TRAF6/CSNK1E信号连接)

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5) — 76.1/100

**核心优势**:
1. 极度新颖: PubMed 仅 19 篇
2. IRBIT 家族成员，具有非酶信号功能
3. PDB 实验结构支撑
4. DNMT 关联暗示表观遗传交叉
5. 实验 PPI 含 TRAF6/CSNK1E 信号激酶

**风险/不确定性**:
1. HPA 主定位为 Cytosol，Nucleoplasm 仅为附加
2. 功能主要为胞质 NBCe1-B 调控
3. 核功能直接证据缺乏
4. 26.5% 无序区域可能影响结构研究

**下一步建议**:
- [ ] 验证 AHCYL2 的核定位比例及其调控条件
- [ ] 探索 AHCYL2-DNMT 关联的表观遗传意义
- [ ] 分析 AHCYL1/AHCYL2 在 IRBIT 信号网络中的功能分工

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96HN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96HN2
- PDB: https://www.rcsb.org/structure/3GVP
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AHCYL2%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000158467-AHCYL2
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/
