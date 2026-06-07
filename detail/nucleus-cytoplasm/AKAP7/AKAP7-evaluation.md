---
type: protein-evaluation
gene: "AKAP7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AKAP7 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AKAP7 / AKAP18 |
| 蛋白大小 | 348 aa / 39.5 kDa |
| UniProt ID | Q9P0M2 |
| 蛋白全名 | A-kinase anchor protein 7 isoform gamma |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Vesicles |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA IF显示Vesicles；UniProt注释Nucleus(by similarity)+Cytoplasm(experimental)；GO-CC有nucleus |
| 蛋白大小 | 7/10 | ×1 | 7 | 348aa/39.5kDa，较小但含完整功能域 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 (21-40→8) |
| 三维结构 | 7/10 | ×3 | 21 | pLDDT=76.7；PDB 4ZP3/5JJ2 (PKA-RII结合域晶体结构) |
| 调控结构域 | 7/10 | ×2 | 14 | IPR019510 PKA-RII binding；核心cAMP/PKA信号调控 |
| PPI网络 | 7/10 | ×3 | 21 | PRKAR2A(0.963实验), PRKACA(0.965实验)；强PKA通路PPI |
| **加权总分** | | | **127/180**** | |
| **归一化总分 (÷1.83)** | | | **69.4/100**** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Vesicles (main) | Approved |
| UniProt | Nucleus (by similarity), Cytoplasm (experimental) | |
| GO-CC | GO:0005829 (cytosol, IDA), GO:0005634 (nucleus, IEA), GO:0098686 (hippocampal mossy fiber to CA3 synapse) | |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

#### 3.2 蛋白大小评估

348 aa / 39.5 kDa。蛋白较小但功能完整，含 PKA-RII 结合域和核定位相关结构。紧凑型信号支架蛋白，实验操作便利。**评分: 7/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 29 |
| PubMed symbol_only | 33 |
| 别名 | AKAP18 |
| 主要方向 | PKA信号、ENaC调控、神经元功能、血小板活化 |

**评价**: PubMed 29 篇 (strict)，中等新颖度。AKAP7 在 PKA 信号空间调控中重要，但研究规模有限。**评分: 8/10** (21-40篇)。

**关键文献**:
1. Jones BW et al. (2016). "Targeted deletion of AKAP7 in dentate granule cells impairs spatial discrimination." *eLife*. PMID: 27911261 — 神经元功能
2. Johnson KR et al. (2012). "Molecular evolution of A-kinase anchoring protein (AKAP)-7." *BMC Evol Biol*. PMID: 22834419
3. Khalil JS et al. (2024). "Protein Kinase A Regulates Platelet Phosphodiesterase 3A through an A-Kinase Anchoring Protein Dependent Manner." *Cells*. PMID: 38994957
4. Kotaki R et al. (2020). "Overexpression of miR-669m inhibits erythroblast differentiation." *Sci Rep*. PMID: 32782283
5. Goldstein SA et al. (2024). "Hidden evolutionary constraints dictate the retention of coronavirus accessory genes." *Curr Biol*. PMID: 39566499

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 76.7 |
| pLDDT > 90 (Very High) | 54.0% |
| pLDDT 70-90 (High) | 12.4% |
| pLDDT 50-70 (Medium) | 7.8% |
| pLDDT < 50 (Low) | 25.9% |
| 有序区域 (pLDDT>70) | 66.4% |
| 实验结构 (PDB) | 4ZP3 (X-ray 2.63A), 5JJ2 (X-ray 1.25A) — PKA-RII结合域 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR019510 (A-kinase anchor protein, PKA-RII binding); IPR019511 (A-kinase anchoring protein); IPR052641 (AKAP7 family); IPR009097 (cAMP-dependent protein kinase regulator) |
| Pfam | PF10469 (AKAP7 2',5'-RNA ligase-like domain); PF10470 (AKAP7 NLS/RII binding) |

AKAP7 是经典 A-kinase anchoring protein，将 PKA 靶向特异性亚细胞位置。含 PKA-RII 结合域和 NLS-like 序列。通过调控 ENaC 通道和 cAMP 信号参与膜兴奋性调控。AKAP 家族作为信号组织者具有重要调控功能。**评分: 7/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (top 10):

| Partner | Score | 实验证据 | 功能类别 |
|---------|-------|---------|---------|
| PRKACA | 0.965 | 0.806 | PKA催化亚基 |
| PRKAR2A | 0.963 | 0.961 | PKA II型调节亚基 |
| PRKACB | 0.963 | 0.796 | PKA催化亚基β |
| PRKACG | 0.931 | 0.622 | PKA催化亚基γ |
| PRKAR2B | 0.926 | 0.839 | PKA II型调节亚基β |
| AKAP1 | 0.924 | 0 | 线粒体AKAP |
| CACNA1C | 0.877 | 0 | L型钙通道 |
| PDE4D | 0.872 | 0 | cAMP磷酸二酯酶 |
| AKAP5 | 0.849 | 0 | 膜AKAP |
| YBEY | 0.832 | 0.831 | 核糖体成熟, 实验互作 |

**IntAct 实验互作**: PRKACA (TAP), PRKACB (TAP), PRKAR1B (Y2H array), PRKAR2B (PCA), SPA17 (Y2H array), ROPN1L (validated Y2H), SNRPE (co-IP)

**PPI 互证分析**: PPI 网络核心为 PKA 全酶复合体 (催化+调节亚基)，实验证据丰富。PRKAR2A 和 PRKAR2B 的强实验互作确认了 AKAP7 作为 PKA 锚定蛋白的核心功能。额外伙伴 YBEY, SPA17, SNRPE 拓展了功能网络。**评分: 7/10**。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5) — 70.6/100

**核心优势**:
1. PKA 信号通路核心支架蛋白
2. PKA-RII 结合域有高分辨率晶体结构
3. 强 PKA 全酶复合体 PPI
4. PPI 实验证据丰富

**风险/不确定性**:
1. HPA IF 主定位为 Vesicles，核定位仅由 UniProt 推断
2. 蛋白较小 (348 aa)
3. 信号通路虽经典但非染色质/转录调控
4. 25.9% 无序区域

**下一步建议**:
- [ ] 确认 AKAP7 在目标细胞中的核质分布
- [ ] 探索非 PKA 伙伴 (YBEY/SPA17) 的功能意义

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P0M2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P0M2
- PDB: https://www.rcsb.org/structure/4ZP3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AKAP7%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000118507-AKAP7
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000118507-AKAP7/subcellular

![](https://images.proteinatlas.org/27200/1805_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27200/1805_C1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/27200/1886_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27200/1886_F4_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P0M2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43687 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052641;IPR019511; |
| Pfam | PF10470; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000118507-AKAP7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PRKACA | Biogrid, Opencell | true |
| SNRPF | Biogrid, Opencell | true |
| SPA17 | Intact, Biogrid | true |
| MEPCE | Biogrid | false |
| PRKACB | Biogrid | false |
| PRKAR1B | Biogrid | false |
| PRKAR2A | Biogrid | false |
| PRKAR2B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
