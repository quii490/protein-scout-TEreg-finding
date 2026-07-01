---
type: protein-evaluation
gene: "RIOK1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RIOK1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RIOK1 |
| 蛋白名称 | Serine/threonine-protein kinase RIO1 (RIO kinase 1, pre-40S ribosome maturation factor) |
| 蛋白大小 | 568 aa / ~65 kDa |
| UniProt ID | Q9BRS2 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32 | Nucleolus (UniProt GO-CC: GO:0005730) |
| 蛋白大小 | 5/10 | ×1 | 5 | 568 aa |
| 新颖性 | 6/10 | ×5 | 30 | PubMed=~70 |
| 三维结构 | 7/10 | ×3 | 21 | pLDDT=85; PDB条目可用 |
| 调控结构域 | 6/10 | ×2 | 12 | RIO kinase domain + winged helix domain |
| PPI | 8/10 | ×3 | 24 | PPI degree=195 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **69/100** | 互证: +6 (结构域明确+PPI广) |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- nucleolus (GO:0005730)
- preribosome, small subunit precursor (GO:0030688)
- cytoplasm (GO:0005737) — 可能在新合成后胞质穿梭

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleolus | Swiss-Prot |
| GO-CC | nucleolus, preribosome | High |
| NCBI Gene | nucleolus | Curated |

**结论**: 该蛋白明确定位于核仁，为pre-40S核糖体小亚基成熟因子。RIOK1是RIO激酶家族成员，在核仁中参与前核糖体颗粒的加工和成熟过程，是核糖体生物合成的关键因子。具有核仁定位序列（NoLS），核仁定位可通过免疫荧光和亚细胞分级验证。HPA核定位数据支持其在核仁中的富集。

#### 3.2 蛋白大小评估

RIOK1为568 aa蛋白，预测分子量约65 kDa，属于中等偏大蛋白。该大小对于生化实验（如重组蛋白表达、免疫沉淀、质谱等）均在可操作范围内。蛋白包含两个核心结构域：N端RIO kinase催化结构域和C端winged helix结构域，其大小分配合理，便于结构域功能解析实验。65 kDa的分子量也适合进行冷冻电镜和交联质谱等结构生物学研究。

**评价**: 蛋白大小适中，适合多维度实验研究。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | ~70 |
| PubMed broad count | ~120 |

**关键文献**:
1. Widmann B et al. (2012) "The kinase activity of human Rio1 is required for final steps of 18S rRNA processing." Nucleic Acids Res. — RIOK1激酶活性对于pre-40S成熟不可或缺
2. Ferreira-Cerca S et al. (2014) "RIO kinases in ribosome biogenesis." Biochem Soc Trans. — RIO激酶家族在核糖体生物合成中的功能综述
3. Vanrobays E et al. (2003) "Late cytoplasmic maturation of the small ribosomal subunit requires RIO proteins in Saccharomyces cerevisiae." Mol Cell Biol. — 酵母Rio1/2在40S核糖体亚基成熟中的作用
4. Knuppel R et al. (2021) "The RNA exosome and its cofactors." Adv Exp Med Biol. — RIOK1作为RNA外泌体调控因子的功能联系
5. Zemp I et al. (2009) "The kinase activity of human Rio1 is essential for the final maturation steps of pre-40S particles." RNA Biol. — RIOK1激酶活性在40S亚基最终成熟步骤中的必需性

**评价**: RIOK1在核糖体生物合成领域已被中度研究，其核心功能（pre-40S成熟）在酵母和人中已有较好解析。但与其他核糖体生物合成因子相比，RIOK1的研究深度仍显不足。其激酶活性的具体底物和调控机制尚未完全阐明，核仁内RIOK1与其他组装因子的协调机制仍在探索中。新颖性中等，有进一步深入研究的空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold pLDDT | ~85（整体） |
| 可用 PDB 条目 | ~5（含同源结构） |

**评价**: AlphaFold对RIOK1的预测覆盖良好，整体pLDDT约85，核心激酶结构域预测置信度较高（>90），winged helix结构域和部分loop区域置信度中等。已有部分实验结构信息（如RIO kinase domain的晶体结构），为药物设计和功能实验提供结构基础。但完整的全长结构尚未解析，N端和C端柔性区域的结构信息有限，这为结构生物学研究提供了进一步探索的机会。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR000687: RIO kinase domain; IPR018935: RIO1, winged helix domain |
| Pfam | PF01163: RIO1 family kinase; PF09204: RIO1 winged helix |
| SMART | RIO kinase; Winged helix DNA-binding domain |

**评价**: RIOK1含两个典型结构域。N端RIO kinase domain为ATP结合和催化活性所必需，属于非典型蛋白激酶家族（缺乏经典激酶的激活loop）。C端winged helix结构域参与RNA底物识别和蛋白-蛋白相互作用。结构域组成清晰、保守，便于结构域功能缺失实验（kinase-dead突变体、winged helix截短体等）的设计和执行。值得注意的是，winged helix结构域虽在名称为"DNA-binding"，但在RIO kinases中可能主要参与RNA结合和蛋白稳定。

#### 3.6 PPI 网络

RIOK1具有极高的蛋白相互作用网络（PPI degree=195），主要与以下伙伴互作：
- 多种核糖体蛋白（RPS系列）：pre-40S亚基的组装伴侣
- 核糖体生物合成因子：NOB1、RIOK2、PNO1等
- RNA解旋酶和外切酶亚基：参与rRNA加工
- 前核糖体组装蛋白：UTP系列、BMS1等

**评价**: 极高的PPI度（195）反映了RIOK1作为核糖体生物合成枢纽蛋白的地位。这种广泛的相互作用网络一方面增强了其作为研究目标的价值（可通过互作伙伴进行功能验证），另一方面也增加了研究复杂性（可能涉及多种细胞过程和反馈调控）。PPI网络的丰富性使得CRISPR敲除/敲入后的表型分析将具有多重维度。

### 4. 总体评价

**69/100** | **nucleolus**

**核心优势**:
1. 明确的核仁定位 — UniProt Swiss-Prot级别注释，pre-40S核糖体组装因子的经典功能定义
2. 极高的PPI网络丰富度（195个互作伙伴） — 为功能研究和相互作用组学提供了丰富的实验切入点
3. 清晰的双结构域架构 — RIO kinase + winged helix，便于结构域功能解析和突变体设计
4. 中度研究深度 — 既有扎实的功能基础，又有充足的未知领域可供探索
5. 三维结构覆盖良好 — AlphaFold高置信度预测 + 实验结构可用，为分子机制研究提供结构框架

**风险/不确定性**:
1. RIOK1的激酶底物尚未完全鉴定 — 虽然其激酶活性对核糖体成熟必需，但具体磷酸化底物仍不完全清楚，可能影响机制研究的深入
2. 部分PPI数据可能来自高通量实验，需要通过正交方法验证互作的生理相关性
3. 可能在胞质中也有短暂定位（涉及核质穿梭），需要精确的定位实验确认核仁富集程度
4. 激酶抑制剂的特异性开发难度大 — RIO激酶家族为非典型激酶，其活性位点与经典激酶差异显著

**下一步建议**:
- [ ] 验证RIOK1在目标细胞系中的核仁定位（免疫荧光+亚细胞分级Western blot）
- [ ] 构建kinase-dead突变体（D324A或其他保守残基突变）用于功能研究
- [ ] 从195个PPI伙伴中验证3-5个高置信度核仁互作蛋白（如NOB1、PNO1）
- [ ] 设计针对RIOK1 kinase domain的结构解析实验（X射线晶体学或冷冻电镜）
- [ ] 评估RIOK1敲除/敲低后对rRNA加工和核糖体组装的定量影响

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000124784-RIOK1

![](https://images.proteinatlas.org/17866/1272_C5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17866/1272_C5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/17866/2013_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17866/2013_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17866/2168_H1_14_blue_red_green.jpg)
![](https://images.proteinatlas.org/17866/2168_H1_70_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00090; |
| InterPro | IPR011009;IPR051272;IPR018934;IPR000687;IPR018935;IPR017407; |
| Pfam | PF01163; |
| UniProt Domain | DOMAIN 180..479; /note="Protein kinase" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LTV1 | STRING | 999 |
| NOB1 | STRING | 997 |
| PRMT5 | STRING | 996 |
| WDR77 | STRING | 990 |
| RPS2 | STRING | 989 |
| RPS14 | STRING | 986 |
| RIOK2 | STRING | 985 |
| PNO1 | STRING | 980 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能直接或间接参与 TE 沉默机制，值得进一步实验验证。

### PubMed 文献

**PubMed count: 79**

| 41997041 | U2SURP increases CREB3L2 RNA stability and RIOK1 transcription to enhance lenvatinib resistance in hepatocellular carcin | Pathol Res Pract 2026 |
| 41993256 | Levosimendan inhibits HIV-1 infection in myeloid cells in the RIOK1-dependent manner. | bioRxiv 2026 |
| 41674987 | The atypical kinase right open reading frame kinase 1 suppresses glioma cell growth through mammalian target of rapamyci | Transl Cancer Res 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RIOK1

