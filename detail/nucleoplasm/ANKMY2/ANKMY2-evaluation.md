---
type: protein-evaluation
gene: "ANKMY2"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKMY2

Q8IV38 | Ankyrin repeat and MYND domain-containing protein 2 | 441aa | pLDDT 86.5 | PM=14 | norm=66.7/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16 |
| 蛋白大小 | 6/10 | ×1 | 6 |
| 研究新颖性 | 10/10 | ×5 | 50 |
| 三维结构 | 7/10 | ×3 | 21 |
| 调控结构域 | 5/10 | ×2 | 10 |
| PPI 网络 | 7/10 | ×3 | 21 |
| **加权总分** | | | **124/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 14 | | |
| **归一化总分 (÷1.83)** | | | **67.8/100** |

**UniProt**: Q8IV38 — Cell projection, cilium (ECO:0000250). GO-CC: cilium (IEA:UniProtKB-SubCell). UniProt interaction: TINF2.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 核定位评定
HPA 主定位 Cytosol (Approved)，额外定位 Nucleoplasm。UniProt 自身注释为纤毛定位 (cilium)，无核定位信息。HPA 将 Nucleoplasm 列为 additional location，reliability 为 Approved，表明 IF 信号中观察到核质分布但非主导。由于主定位不在核内且 UniProt 不支持核定位，核定位特异性评为 4/10。

### 蛋白大小
441 aa，49.3 kDa，中等大小蛋白。包含 Ankyrin repeat (IPR002110/IPR036770) 和 MYND domain (IPR002893)。分子量适合常规生化分析，评为 6/10。

### 研究新颖性
PubMed strict count = 14（≤20 档），研究稀缺。关键方向：(1) 纤毛生物学 — PMID 37943875 报道 ANKMY2 在 hedgehog 通路纤毛调控中的上下文依赖功能，PMID 41474822 发现 ANKMY2 缺失抑制肾囊肿生成，PMID 40501923 关联纤毛腺苷酸环化酶靶向与 ADPKD；(2) 阿尔茨海默病血浆肽段 — PMID 34182925；(3) circRNA — PMID 33095438 报道 Circ_ANKMY2 通过 miR-106b-5p/FOXP1 轴调控颞叶癫痫。肾纤毛病变与纤毛信号转导是其主要研究方向。评为 10/10（高新颖性）。

### PDB 结构
PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。
AlphaFold v6: mean_pLDDT = 86.5，pct_gt_90 = 77.3%，pct_70_90 = 6.6%，pct_lt_50 = 12.9%。结构预测置信度优秀，77% 残基 pLDDT > 90。无实验 PDB 结构。AlphaFold 模型质量较高，适合用于结构分析。评为 7/10。

### 调控结构域
InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR052452) + MYND zinc finger (IPR002893)。Pfam: Ank_2 (PF12796) + zf-MYND (PF01753)。MYND 结构域为锌指型蛋白-蛋白互作模块，常见于转录调控因子。ANK 重复提供支架功能，MYND 赋予潜在转录调控活性，组合具有功能多样性。评为 5/10。

### PPI 网络
STRING: AGO3 (0.885, experimental 0.782)、FKBP8 (0.719, exp 0.611)、GUCY1A1 (0.628, exp 0.622) 等 15 个伙伴。IntAct: 15 条互作记录，包括 GUCY2D (co-IP)、AGO3 (co-IP)、ADCY3/6 (co-IP)、HSP90AA1 (co-IP)、FKBP8 (co-IP) 等，多条源自 Nature 2017 大规模 co-IP 研究 (PMID 28514442)。UniProt: TINF2 (2 experiments)。PPI 网络由多项大规模实验支撑，AGO 家族蛋白与纤毛腺苷酸环化酶的互作尤为突出。评为 7/10。

### 关键文献
- PMID 41474822: Lack of ANKMY2 suppresses kidney cystogenesis in ADPKD (PLoS Genet, 2025)
- PMID 37943875: Context-dependent ciliary regulation of hedgehog pathway (PLoS Genet, 2023)
- PMID 33095438: Circ_ANKMY2 regulates temporal lobe epilepsy via miR-106b-5p/FOXP1 (Neurochem Res, 2020)

### 人工复核建议
核定位为 HPA additional location，主定位 Cytosol/纤毛，若以核蛋白研究为目标则该蛋白核定位偏弱。纤毛-核质穿梭可能在某些条件下发生，但并非稳态核定位。建议关注其在纤毛信号转导中的角色及其与肾纤毛病的关系。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000106524-ANKMY2/subcellular

![](https://images.proteinatlas.org/67100/1250_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/67100/1250_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/67100/1255_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/67100/1255_G5_3_red_green.jpg)
![](https://images.proteinatlas.org/67100/1924_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/67100/1924_G12_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
